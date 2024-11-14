import day16
import unittest

class Day16(unittest.TestCase):
    def test_part1(self):
        lines = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
        """
        self.assertEqual(day16.solvePart1(lines.splitlines()), 46)
    def test_part2(self):
        lines = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
        """
        self.assertEqual(day16.solvePart2(lines.splitlines()), 51)

if __name__ == '__main__':
    unittest.main()
