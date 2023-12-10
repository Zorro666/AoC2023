import day07
import unittest

class Day07(unittest.TestCase):
    def test_part1(self):
        lines = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
        """
        self.assertEqual(day07.solvePart1(lines.splitlines()), 6440)
    def test_rank_hand6(self):
        self.assertEqual(day07.rank_hand("AAAAA"), 6)
    def test_rank_hand5(self):
        self.assertEqual(day07.rank_hand("9A999"), 5)
    def test_rank_hand4(self):
        self.assertEqual(day07.rank_hand("AA999"), 4)
    def test_rank_hand3(self):
        self.assertEqual(day07.rank_hand("83889"), 3)
    def test_rank_hand2(self):
        self.assertEqual(day07.rank_hand("32329"), 2)
    def test_rank_hand1(self):
        self.assertEqual(day07.rank_hand("K23K9"), 1)
    def test_rank_hand0(self):
        self.assertEqual(day07.rank_hand("AKQT9"), 0)
    def test_hand_greater0(self):
        h_i = "T55J5"
        h_j = "QQQJA"
        r_i = day07.rank_hand(h_i)
        r_j = day07.rank_hand(h_j)
        day07.prepare1()
        self.assertEqual(day07.hand_greater(r_i, r_j, h_i, h_j), False)
    def test_hand_greater1(self):
        h_i = "QQQJA"
        h_j = "T55J5"
        r_i = day07.rank_hand(h_i)
        r_j = day07.rank_hand(h_j)
        day07.prepare1()
        self.assertEqual(day07.hand_greater(r_i, r_j, h_i, h_j), True)
    def test_hand_greater2(self):
        h_i = "KK3KK"
        h_j = "22522"
        r_i = day07.rank_hand(h_i)
        r_j = day07.rank_hand(h_j)
        day07.prepare1()
        self.assertEqual(day07.hand_greater(r_i, r_j, h_i, h_j), True)
    def test_part2(self):
        lines = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
        """
        self.assertEqual(day07.solvePart2(lines.splitlines()), 5905)

if __name__ == '__main__':
    unittest.main()
