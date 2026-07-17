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
