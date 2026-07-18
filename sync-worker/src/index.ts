import { Hono } from "hono";
import { cors } from "hono/cors";
import { rateLimiter } from "hono-rate-limiter";
import { mergeUpdate } from "./sync";
import { makeCode } from "./code";

// Bindings come from `wrangler types` (worker-configuration.d.ts, global `Env`),
// so they track wrangler.toml — regenerate with `pnpm cf-typegen` after config changes.
const app = new Hono<{ Bindings: Env }>();

app.use("*", cors({
  origin: "*",
  allowMethods: ["GET", "POST", "OPTIONS"],
  allowHeaders: ["Content-Type", "X-State-Vector"],
  exposeHeaders: ["X-Sync-Code"],
  maxAge: 86400,
}));

app.use("*", rateLimiter<{ Bindings: Env }>({
  binding: (c) => c.env.RATE_LIMITER,
  keyGenerator: (c) => c.req.header("cf-connecting-ip") ?? "anon",
}));

const bin = (u: Uint8Array) =>
  new Response(u, { headers: { "Content-Type": "application/octet-stream" } });

// Decode the optional X-State-Vector request header (base64 state vector).
// Anything undecodable is treated as absent → callers fall back to a full reply.
function decodeSV(h: string | undefined): Uint8Array | undefined {
  if (!h) return undefined;
  try {
    const s = atob(h);
    const u = new Uint8Array(s.length);
    for (let i = 0; i < s.length; i++) u[i] = s.charCodeAt(i);
    return u;
  } catch {
    return undefined;
  }
}

app.post("/new", async (c) => {
  const incoming = new Uint8Array(await c.req.arrayBuffer());
  const state = mergeUpdate(null, incoming);
  let code = "";
  for (let i = 0; i < 6; i++) {
    const cand = makeCode(4);
    if (!(await c.env.SYNC_KV.get("r:" + cand))) { code = cand; break; }
  }
  if (!code) return c.json({ error: "code space exhausted" }, 500);
  await c.env.SYNC_KV.put("r:" + code, state);
  const res = bin(state);
  res.headers.set("X-Sync-Code", code);
  return res;
});

app.get("/r/:code", async (c) => {
  const code = c.req.param("code").toLowerCase();
  const stored = await c.env.SYNC_KV.get("r:" + code, "arrayBuffer");
  if (!stored) return c.json({ error: "not found" }, 404);
  return bin(new Uint8Array(stored));
});

app.post("/r/:code", async (c) => {
  const code = c.req.param("code").toLowerCase();
  const stored = await c.env.SYNC_KV.get("r:" + code, "arrayBuffer");
  if (!stored) return c.json({ error: "not found" }, 404);
  const incoming = new Uint8Array(await c.req.arrayBuffer());
  const sv = decodeSV(c.req.header("X-State-Vector"));
  const full = mergeUpdate(new Uint8Array(stored), incoming);
  let reply: Uint8Array;
  if (sv) {
    try {
      reply = mergeUpdate(full, new Uint8Array(0), sv);
    } catch {
      reply = full; // decodable-but-invalid SV → full reply
    }
  } else {
    reply = full;
  }
  await c.env.SYNC_KV.put("r:" + code, full);
  return bin(reply);
});

// Pull: the client sends its state vector as the body and gets back only the diff
// it is missing (the Yjs SyncStep1/SyncStep2 handshake flattened into HTTP).
app.post("/r/:code/sync", async (c) => {
  const code = c.req.param("code").toLowerCase();
  const stored = await c.env.SYNC_KV.get("r:" + code, "arrayBuffer");
  if (!stored) return c.json({ error: "not found" }, 404);
  const sv = new Uint8Array(await c.req.arrayBuffer());
  let out: Uint8Array;
  try {
    out = mergeUpdate(new Uint8Array(stored), new Uint8Array(0), sv);
  } catch {
    out = new Uint8Array(stored); // undecodable SV → full state; the client heals
  }
  return bin(out);
});

export default app;
