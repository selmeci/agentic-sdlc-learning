import { describe, it, expect } from "vitest";
import * as Y from "yjs";
import { mergeUpdate } from "../src/sync";

function update(fn: (d: Y.Doc) => void): Uint8Array {
  const d = new Y.Doc();
  fn(d);
  return Y.encodeStateAsUpdate(d);
}
function progressOf(bytes: Uint8Array): Record<string, unknown> {
  const d = new Y.Doc();
  Y.applyUpdate(d, bytes);
  return d.getMap("progress").toJSON();
}
function seenOf(bytes: Uint8Array): Record<string, unknown> {
  const d = new Y.Doc();
  Y.applyUpdate(d, bytes);
  return d.getMap("seen").toJSON();
}

describe("mergeUpdate", () => {
  it("round-trips a single update", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "done"));
    expect(progressOf(mergeUpdate(null, a))).toEqual({ "eng-1": "done" });
  });

  it("merges two updates and converges regardless of apply order", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "done"));
    const b = update((d) => d.getMap("progress").set("eng-2", "studying"));
    const ab = progressOf(mergeUpdate(mergeUpdate(null, a), b));
    const ba = progressOf(mergeUpdate(mergeUpdate(null, b), a));
    expect(ab).toEqual({ "eng-1": "done", "eng-2": "studying" });
    expect(ab).toEqual(ba);
  });

  it("unions grow-only seen-set keys", () => {
    const a = update((d) => d.getMap("seen").set("e1ov:0", true));
    const b = update((d) => d.getMap("seen").set("e1ov:1", true));
    expect(seenOf(mergeUpdate(mergeUpdate(null, a), b))).toEqual({ "e1ov:0": true, "e1ov:1": true });
  });

  it("treats a null/empty stored doc as a fresh doc", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "studying"));
    expect(progressOf(mergeUpdate(new Uint8Array(0), a))).toEqual({ "eng-1": "studying" });
  });
});

describe("mergeUpdate with replySV", () => {
  it("returns only the diff the requester is missing", () => {
    const a = update((d) => d.getMap("progress").set("a", "studying"));
    const b = update((d) => d.getMap("progress").set("b", "done"));
    const requester = new Y.Doc();
    Y.applyUpdate(requester, a);
    const stored = mergeUpdate(mergeUpdate(null, a), b);
    const full = mergeUpdate(stored, new Uint8Array(0));
    const diff = mergeUpdate(stored, new Uint8Array(0), Y.encodeStateVector(requester));
    expect(diff.byteLength).toBeLessThan(full.byteLength);
    // the diff carries only structs the requester lacked (b's client, not a's)
    const diffClients = new Set(Y.decodeStateVector(Y.encodeStateVectorFromUpdate(diff)).keys());
    for (const id of Y.decodeStateVector(Y.encodeStateVectorFromUpdate(a)).keys()) {
      expect(diffClients.has(id)).toBe(false);
    }
    Y.applyUpdate(requester, diff);
    expect(requester.getMap("progress").toJSON()).toEqual({ a: "studying", b: "done" });
  });

  it("returns a valid empty diff when the requester is converged", () => {
    const a = update((d) => d.getMap("progress").set("a", "done"));
    const requester = new Y.Doc();
    Y.applyUpdate(requester, a);
    const diff = mergeUpdate(a, new Uint8Array(0), Y.encodeStateVector(requester));
    Y.applyUpdate(requester, diff); // must not throw
    expect(requester.getMap("progress").toJSON()).toEqual({ a: "done" });
  });

  it("treats an empty replySV as absent (full re-encode)", () => {
    const a = update((d) => d.getMap("progress").set("a", "done"));
    expect(mergeUpdate(a, new Uint8Array(0), new Uint8Array(0)))
      .toEqual(mergeUpdate(a, new Uint8Array(0)));
  });
});
