import day05
import unittest

class Day05(unittest.TestCase):
    def test_part1(self):
        lines = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
        self.assertEqual(day05.solvePart1(lines.splitlines()), 142)
    def test_part2(self):
        lines = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
        self.assertEqual(day05.solvePart2(lines.splitlines()), 281)

if __name__ == '__main__':
    unittest.main()
