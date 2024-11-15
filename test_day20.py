import day20
import unittest

class Day20(unittest.TestCase):
    lines1 = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
    lines2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> rx
"""
    def test_part1_1(self):
        self.assertEqual(day20.solvePart1(self.lines1.splitlines()), 32000000)

    def test_part1_2(self):
        self.assertEqual(day20.solvePart1(self.lines2.splitlines()), 11687500)

    def test_part2(self):
        self.assertEqual(day20.solvePart2(self.lines2.splitlines()), 1)

if __name__ == '__main__':
    unittest.main()
