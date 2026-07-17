const ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789";

// Slight modulo bias (256 % 36) is negligible for a low-stakes study-tool code.
export function makeCode(len = 4): string {
  const bytes = new Uint8Array(len);
  crypto.getRandomValues(bytes);
  let out = "";
  for (let i = 0; i < len; i++) out += ALPHABET[bytes[i] % ALPHABET.length];
  return out;
}
