import day12
import unittest

class Day12(unittest.TestCase):
    def test_part1(self):
        lines = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
        """
        self.assertEqual(day12.solvePart1(lines.splitlines()), 21)
    def test_part2(self):
        lines = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
        """
        self.assertEqual(day12.solvePart2(lines.splitlines()), 281)

if __name__ == '__main__':
    unittest.main()
