import { describe, it, expect } from "vitest";
import { makeCode } from "../src/code";

describe("makeCode", () => {
  it("is 4 chars from the allowed alphabet by default", () => {
    for (let i = 0; i < 200; i++) expect(makeCode()).toMatch(/^[a-z0-9]{4}$/);
  });
});
