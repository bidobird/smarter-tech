import { describe, expect, it } from "vitest";
import { sort } from "../src/sort.js";

describe("sort(width, height, length, mass)", () => {
  it("returns STANDARD when not bulky and not heavy", () => {
    expect(sort(10, 10, 10, 1)).toBe("STANDARD");
  });

  it("treats volume >= 1,000,000 cm³ as bulky (SPECIAL if not heavy)", () => {
    expect(sort(100, 100, 100, 19.999)).toBe("SPECIAL");
  });

  it("treats any dimension >= 150 cm as bulky (SPECIAL if not heavy)", () => {
    expect(sort(150, 10, 10, 0)).toBe("SPECIAL");
    expect(sort(10, 150, 10, 0)).toBe("SPECIAL");
    expect(sort(10, 10, 150, 0)).toBe("SPECIAL");
  });

  it("treats mass >= 20 kg as heavy (SPECIAL if not bulky)", () => {
    expect(sort(10, 10, 10, 20)).toBe("SPECIAL");
  });

  it("returns REJECTED when both bulky and heavy", () => {
    expect(sort(150, 10, 10, 20)).toBe("REJECTED");
    expect(sort(100, 100, 100, 20)).toBe("REJECTED");
  });

  it("handles values just below thresholds as STANDARD", () => {
    // volume 99.99^3 = 999,700.029999 (not bulky by volume)
    expect(sort(99.99, 99.99, 99.99, 19.999)).toBe("STANDARD");
    expect(sort(149.999, 10, 10, 0)).toBe("STANDARD");
  });

  it("throws on non-finite or negative inputs", () => {
    expect(() => sort(Number.NaN, 1, 1, 1)).toThrow();
    expect(() => sort(1, 1, 1, Number.POSITIVE_INFINITY)).toThrow();
    expect(() => sort(-1, 1, 1, 1)).toThrow();
    expect(() => sort(1, 1, 1, -1)).toThrow();
  });
});

