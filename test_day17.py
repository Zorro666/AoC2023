import day17
import unittest

class Day17(unittest.TestCase):
    lines = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
    def test_part1(self):
        self.assertEqual(day17.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day17.solvePart2(self.lines.splitlines()), 94)

if __name__ == '__main__':
    unittest.main()
