import day14
import unittest

class Day14(unittest.TestCase):
    input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
        """.splitlines()
    def test_part1(self):
        self.assertEqual(day14.solvePart1(self.input), 136)
    def test_cycle1(self):
        (grid, w, h) = day14.parse(self.input)
        day14.runCycle(grid, w, h)
        expected = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
"""
        y = h - 1
        for l in expected.splitlines():
            l = l.strip()
            if len(l) == 0:
                continue
            e = list(l)
            self.assertEqual(grid[y], e)
            y -= 1
    def test_cycle2(self):
        (grid, w, h) = day14.parse(self.input)
        day14.runCycle(grid, w, h)
        day14.runCycle(grid, w, h)
        expected = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
"""
        y = h - 1
        for l in expected.splitlines():
            l = l.strip()
            if len(l) == 0:
                continue
            e = list(l)
            self.assertEqual(grid[y], e)
            y -= 1
    def test_cycle3(self):
        (grid, w, h) = day14.parse(self.input)
        day14.runCycle(grid, w, h)
        day14.runCycle(grid, w, h)
        day14.runCycle(grid, w, h)
        expected = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
"""
        y = h - 1
        for l in expected.splitlines():
            l = l.strip()
            if len(l) == 0:
                continue
            e = list(l)
            self.assertEqual(grid[y], e)
            y -= 1
    def test_part2(self):
        self.assertEqual(day14.solvePart2(self.input), 64)

if __name__ == '__main__':
    unittest.main()
