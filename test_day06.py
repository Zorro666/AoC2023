import day06
import unittest

class Day06(unittest.TestCase):
    lines = """
Time:      7  15   30
Distance:  9  40  200
        """
    def test_part1(self):
        self.assertEqual(day06.solvePart1(self.lines.splitlines()), 288)
    def test_part2(self):
        self.assertEqual(day06.solvePart2(self.lines.splitlines()), 71503)

if __name__ == '__main__':
    unittest.main()
