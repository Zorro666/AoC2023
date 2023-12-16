import day10
import unittest

class Day10(unittest.TestCase):
    def test_part1_1(self):
        lines = """
.....
.S-7.
.|.|.
.L-J.
.....
        """
        self.assertEqual(day10.solvePart1(lines.splitlines()), 4)
    def test_part1_2(self):
        lines = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
        """
        self.assertEqual(day10.solvePart1(lines.splitlines()), 8)
    def test_part2_1(self):
        lines = """
.....
.S-7.
.|.|.
.L-J.
.....
        """
        self.assertEqual(day10.solvePart2(lines.splitlines()), 1)
    def test_part2_2(self):
        lines = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
        """
        self.assertEqual(day10.solvePart2(lines.splitlines()), 4)
    def test_part2_3(self):
        lines = """
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
        """
        self.assertEqual(day10.solvePart2(lines.splitlines()), 4)
    def test_part2_4(self):
        lines = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
        """
        self.assertEqual(day10.solvePart2(lines.splitlines()), 8)
    def test_part2_5(self):
        lines = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
        """
        self.assertEqual(day10.solvePart2(lines.splitlines()), 10)

if __name__ == '__main__':
    unittest.main()
