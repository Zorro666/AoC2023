import day08
import unittest

class Day08(unittest.TestCase):
    def test_part1_1(self):
        lines = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
        """
        self.assertEqual(day08.solvePart1(lines.splitlines()), 2)
    def test_part1_2(self):
        lines = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
        """
        self.assertEqual(day08.solvePart1(lines.splitlines()), 6)
    def test_part2(self):
        lines = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
        """
        self.assertEqual(day08.solvePart2(lines.splitlines()), 6)

if __name__ == '__main__':
    unittest.main()
