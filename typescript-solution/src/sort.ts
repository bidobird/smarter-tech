export type Stack = "STANDARD" | "SPECIAL" | "REJECTED";

const VOLUME_BULKY_THRESHOLD_CM3 = 1000000;
const DIMENSION_BULKY_THRESHOLD_CM = 150;
const HEAVY_THRESHOLD_KG = 20;

function ensureFiniteNonNegative(value: number, name: string): void {
  if (!Number.isFinite(value)) {
    throw new TypeError(`${name} must be a finite number`);
  }
  if (value < 0) {
    throw new RangeError(`${name} must be >= 0`);
  }
}

export function sort(
  width: number,
  height: number,
  length: number,
  mass: number
): Stack {
  ensureFiniteNonNegative(width, "width");
  ensureFiniteNonNegative(height, "height");
  ensureFiniteNonNegative(length, "length");
  ensureFiniteNonNegative(mass, "mass");

  const volume = width * height * length;
  const bulky =
    volume >= VOLUME_BULKY_THRESHOLD_CM3 ||
    width >= DIMENSION_BULKY_THRESHOLD_CM ||
    height >= DIMENSION_BULKY_THRESHOLD_CM ||
    length >= DIMENSION_BULKY_THRESHOLD_CM;
  const heavy = mass >= HEAVY_THRESHOLD_KG;

  if (bulky && heavy) return "REJECTED";
  if (bulky || heavy) return "SPECIAL";
  return "STANDARD";
}

