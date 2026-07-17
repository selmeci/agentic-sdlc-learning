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
  allowHeaders: ["Content-Type"],
  exposeHeaders: ["X-Sync-Code"],
  maxAge: 86400,
}));

app.use("*", rateLimiter<{ Bindings: Env }>({
  binding: (c) => c.env.RATE_LIMITER,
  keyGenerator: (c) => c.req.header("cf-connecting-ip") ?? "anon",
}));

const bin = (u: Uint8Array) =>
  new Response(u, { headers: { "Content-Type": "application/octet-stream" } });

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
  const merged = mergeUpdate(new Uint8Array(stored), incoming);
  await c.env.SYNC_KV.put("r:" + code, merged);
  return bin(merged);
});

export default app;
