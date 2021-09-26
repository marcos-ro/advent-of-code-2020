import unittest
import day_02

class TestDay02(unittest.TestCase):
    def test_new_password(self):
        password = day_02.new_password("1-3 a: abcd")
        expected_password = {"range": (1, 3), "character": "a", "plain": "abcd"}
        self.assertEqual(password, expected_password)

    def test_example_01(self):
        fake_input = [
            {"range": (1, 3), "character": "a", "plain": "abcde"},
            {"range": (1, 3), "character": "b", "plain": "cdefg"},
            {"range": (2, 9), "character": "c", "plain": "ccccccccc"}
        ]
        count = day_02.count_by_policy(fake_input, day_02.default_policy)
        self.assertEqual(count, 2)

    def test_example_02(self):
        fake_input = [
            {"range": (1, 3), "character": "a", "plain": "abcde"},
            {"range": (1, 3), "character": "b", "plain": "cdefg"},
            {"range": (2, 9), "character": "c", "plain": "ccccccccc"}
        ]
        count = day_02.count_by_policy(fake_input, day_02.new_policy)
        self.assertEqual(count, 1)

if __name__ == "__main__":
    unittest.main()
