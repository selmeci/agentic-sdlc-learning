import * as Y from "yjs";

// Merge an incoming Yjs update onto the stored encoded state and return the new
// encoded state. Merge is Yjs's applyUpdate — commutative, idempotent, associative.
// When replySV (the requester's state vector) is given, the result is only the diff
// the requester is missing instead of the full state. Deltas and full states apply
// identically on the other end.
export function mergeUpdate(stored: Uint8Array | null, incoming: Uint8Array, replySV?: Uint8Array): Uint8Array {
  const doc = new Y.Doc();
  if (stored && stored.byteLength) Y.applyUpdate(doc, stored);
  if (incoming && incoming.byteLength) Y.applyUpdate(doc, incoming);
  const out = replySV && replySV.byteLength
    ? Y.encodeStateAsUpdate(doc, replySV)
    : Y.encodeStateAsUpdate(doc);
  doc.destroy();
  return out;
}
