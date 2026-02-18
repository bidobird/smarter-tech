import math
import unittest

from src.sort import sort


class TestSort(unittest.TestCase):
    def test_standard_when_not_bulky_or_heavy(self) -> None:
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume_threshold(self) -> None:
        self.assertEqual(sort(100, 100, 100, 19.999), "SPECIAL")

    def test_bulky_by_dimension_threshold(self) -> None:
        self.assertEqual(sort(150, 10, 10, 0), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 0), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 0), "SPECIAL")

    def test_heavy_by_mass_threshold(self) -> None:
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected_when_both_bulky_and_heavy(self) -> None:
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    def test_just_below_thresholds_is_standard(self) -> None:
        self.assertEqual(sort(99.99, 99.99, 99.99, 19.999), "STANDARD")
        self.assertEqual(sort(149.999, 10, 10, 0), "STANDARD")

    def test_invalid_inputs(self) -> None:
        with self.assertRaises(TypeError):
            sort(math.nan, 1, 1, 1)
        with self.assertRaises(TypeError):
            sort(1, 1, 1, math.inf)
        with self.assertRaises(ValueError):
            sort(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            sort(1, 1, 1, -1)
        with self.assertRaises(TypeError):
            sort(True, 1, 1, 1)


if __name__ == "__main__":
    unittest.main()

