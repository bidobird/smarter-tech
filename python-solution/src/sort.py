from __future__ import annotations

import math
from typing import Literal, Union

Stack = Literal["STANDARD", "SPECIAL", "REJECTED"]
Number = Union[int, float]

VOLUME_BULKY_THRESHOLD_CM3 = 1000000
DIMENSION_BULKY_THRESHOLD_CM = 150
HEAVY_THRESHOLD_KG = 20


def _ensure_finite_non_negative(value: Number, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an int or float")
    if not math.isfinite(value):
        raise TypeError(f"{name} must be finite")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")


def sort(width: Number, height: Number, length: Number, mass: Number) -> Stack:
    """
    Dispatch a package into STANDARD, SPECIAL, or REJECTED based on its dimensions and mass.

    Units:
      - width/height/length: centimeters
      - mass: kilograms
    """

    _ensure_finite_non_negative(width, "width")
    _ensure_finite_non_negative(height, "height")
    _ensure_finite_non_negative(length, "length")
    _ensure_finite_non_negative(mass, "mass")

    volume = width * height * length
    bulky = (
        volume >= VOLUME_BULKY_THRESHOLD_CM3
        or width >= DIMENSION_BULKY_THRESHOLD_CM
        or height >= DIMENSION_BULKY_THRESHOLD_CM
        or length >= DIMENSION_BULKY_THRESHOLD_CM
    )
    heavy = mass >= HEAVY_THRESHOLD_KG

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"

