import random
import unittest

from my_utils import mean, median, stdev


class TestMyUtils(unittest.TestCase):
    # ---- mean ----
    def test_mean_basic(self):
        self.assertEqual(mean([1, 2, 3]), 2.0)

    def test_mean_random_positive(self):
        # Property: mean is between min and max for any non-empty list
        for _ in range(25):
            xs = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]
            m = mean(xs)
            self.assertTrue(min(xs) <= m <= max(xs))

    def test_mean_empty_raises(self):
        with self.assertRaises(ValueError):
            mean([])

    # ---- median ----
    def test_median_basic_odd_even(self):
        self.assertEqual(median([1, 2, 3]), 2.0)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_random_order_invariant(self):
        # Property: median does not depend on order of inputs
        for _ in range(25):
            xs = [random.randint(-50, 50) for _ in range(random.randint(1, 21))]
            a = median(xs)
            random.shuffle(xs)
            b = median(xs)
            self.assertEqual(a, b)

    def test_median_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])

    # ---- stdev ----
    def test_stdev_basic(self):
        # Example from A4 step notes: approx 2.138089935
        val = stdev([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(val, 2.138089935, places=6)

    def test_stdev_requires_two(self):
        with self.assertRaises(ValueError):
            stdev([])
        with self.assertRaises(ValueError):
            stdev([1])


if __name__ == "__main__":
    unittest.main()
