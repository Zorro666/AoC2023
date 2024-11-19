import day21
import unittest

class Day21(unittest.TestCase):
    lines = '''
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''
    def test_part1(self):
        self.assertEqual(day21.countLocations(self.lines.splitlines(), [6])[0], 16)
    def test_part2(self):
        maxSteps = [10, 50, 100, 500]
        counts = day21.countLocations(self.lines.splitlines(), maxSteps)
        self.assertEqual(counts[0], 50)
        self.assertEqual(counts[1], 1594)
        self.assertEqual(counts[2], 6536)
        self.assertEqual(counts[3], 167004)
#        self.assertEqual(counts[4], 668697)
#    def test_part2_5000(self):
#        self.assertEqual(day21.countLocations(self.lines.splitlines(), [5000])[0], 16733044)

if __name__ == '__main__':
    unittest.main()
