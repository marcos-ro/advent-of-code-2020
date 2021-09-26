import unittest
import day_04

class TestDay04(unittest.TestCase):
    def test_new_passport(self):
        fake_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm"""
        passport = day_04.new_passport(fake_input)
        expected_passport = {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm"
        }
        self.assertEqual(passport, expected_passport)

    def test_example_01(self):
        fake_input = day_04.new_passports("input/fake_input.txt")
        count = day_04.count_by_policy(fake_input, day_04.default_policy)
        self.assertEqual(count, 2)

    def test_example_valid_passports(self):
        fake_input = day_04.new_passports("input/fake_valid_passports.txt")
        count = day_04.count_by_policy(fake_input, day_04.new_policy)
        self.assertEqual(count, 4)

if __name__ == "__main__":
    unittest.main()
