import unittest
import day_05

class TestDay05(unittest.TestCase):
    def test_example_01(self):
        boarding_passes = [
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL"
        ]
        self.assertEqual(day_05.calculate_max_id(boarding_passes), 820)

if __name__ == "__main__":
    unittest.main()
