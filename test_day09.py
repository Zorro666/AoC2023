import day09
import unittest

class Day09(unittest.TestCase):
    def test_part1(self):
        lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
        """
        self.assertEqual(day09.solvePart1(lines.splitlines()), 114)
    def test_part2(self):
        lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
        """
        self.assertEqual(day09.solvePart2(lines.splitlines()), 2)

if __name__ == '__main__':
    unittest.main()
