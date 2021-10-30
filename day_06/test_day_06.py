import unittest

import day_06

class TestDay06(unittest.TestCase):
    def test_example_01(self):
        groups = day_06.from_file("input/fake_input.txt")
        self.assertEqual(day_06.count_anyone_yes(groups), 11)

    def test_example_02(self):
        groups = day_06.from_file("input/fake_input.txt")
        self.assertEqual(day_06.count_everyone_yes(groups), 6)
