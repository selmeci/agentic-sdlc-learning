import * as Y from "yjs";

// Merge an incoming Yjs update onto the stored encoded state and return the new
// encoded state. Merge is Yjs's applyUpdate — commutative, idempotent, associative.
export function mergeUpdate(stored: Uint8Array | null, incoming: Uint8Array): Uint8Array {
  const doc = new Y.Doc();
  if (stored && stored.byteLength) Y.applyUpdate(doc, stored);
  if (incoming && incoming.byteLength) Y.applyUpdate(doc, incoming);
  const out = Y.encodeStateAsUpdate(doc);
  doc.destroy();
  return out;
}
