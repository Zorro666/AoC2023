import day22
import unittest

class Day22(unittest.TestCase):
    lines = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

    def test_part1(self):
        self.assertEqual(day22.solvePart1(self.lines.splitlines()), 5)

    def test_part2(self):
        self.assertEqual(day22.solvePart2(self.lines.splitlines()), 7)

if __name__ == '__main__':
    unittest.main()
