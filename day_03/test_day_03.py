import unittest
import day_03

class TestDay03(unittest.TestCase):
    def test_example_01(self):
        fake_input = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]
        steps = {"right": 3, "down": 1, "x": 0, "y": 0, "repeat": 2}
        count = day_03.simulate(fake_input, steps)
        self.assertEqual(count, 7)

    def test_example_02(self):
        fake_input = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]
        steps_list = [
            {"right": 1, "down": 1, "x": 0, "y": 0, "repeat": 2},
            {"right": 3, "down": 1, "x": 0, "y": 0, "repeat": 2},
            {"right": 5, "down": 1, "x": 0, "y": 0, "repeat": 2},
            {"right": 7, "down": 1, "x": 0, "y": 0, "repeat": 2},
            {"right": 1, "down": 2, "x": 0, "y": 0, "repeat": 2},
        ]
        product = day_03.simulate_by_steps_list(fake_input, steps_list)
        self.assertEqual(product, 336)

if __name__ == "__main__":
    unittest.main()
