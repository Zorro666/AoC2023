import day13
import unittest

class Day13(unittest.TestCase):
    def test_pattern_score_1(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        self.assertEqual(day13.pattern_score(lines.splitlines(), False), 5)
    def test_pattern_score_2(self):
        lines = """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.pattern_score(lines.splitlines(), True), 100)
    def test_part1(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.solvePart1(lines.splitlines()), 405)
    def test_part2(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.solvePart2(lines.splitlines()), 400)

if __name__ == '__main__':
    unittest.main()
