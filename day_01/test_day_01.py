import unittest
import day_01

class TestDay01(unittest.TestCase):
    def test_example_01(self):
        fake_input = [1721, 979, 366, 299, 675, 1456]
        [result] = day_01.find_by_sum(fake_input, 2, 2020)
        self.assertEqual(result, 514579)

    def test_example_02(self):
         fake_input = [1721, 979, 366, 299, 675, 1456]
         [result] = day_01.find_by_sum(fake_input, 3, 2020)
         self.assertEqual(result, 241861950)
 
if __name__ == "__main__":
    unittest.main()
