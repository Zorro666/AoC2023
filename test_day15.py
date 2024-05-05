import day15
import unittest

class Day15(unittest.TestCase):
    input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    def test_part1(self):
        self.assertEqual(day15.solvePart1(self.input.splitlines()), 1320)
    def test_part2(self):
        self.assertEqual(day15.solvePart2(self.input.splitlines()), 145)

if __name__ == '__main__':
    unittest.main()
