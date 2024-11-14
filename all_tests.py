import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25
import unittest

class Day01(unittest.TestCase):
    def test_part1(self):
        lines = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
        self.assertEqual(day01.solvePart1(lines.splitlines()), 142)
    def test_part2(self):
        lines = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
        self.assertEqual(day01.solvePart2(lines.splitlines()), 281)

class Day02(unittest.TestCase):
    def test_part1(self):
        lines = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
        self.assertEqual(day02.solvePart1(lines.splitlines()), 8)
    def test_part2(self):
        lines = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """
        self.assertEqual(day02.solvePart2(lines.splitlines()), 2286)

class Day03(unittest.TestCase):
    def test_part1(self):
        lines = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        self.assertEqual(day03.solvePart1(lines.splitlines()), 4361)
    def test_part2(self):
        lines = """467+.114..
+..*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        self.assertEqual(day03.solvePart2(lines.splitlines()), 467835)

class Day04(unittest.TestCase):
    def test_part1(self):
        lines = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
        self.assertEqual(day04.solvePart1(lines.splitlines()), 13)
    def test_part2(self):
        lines = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
        self.assertEqual(day04.solvePart2(lines.splitlines()), 30)

class Day05(unittest.TestCase):
    lines = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    def test_part1(self):
        self.assertEqual(day05.solvePart1(self.lines.splitlines()), 35)
    def test_part2(self):
        self.assertEqual(day05.solvePart2(self.lines.splitlines()), 46)

class Day06(unittest.TestCase):
    lines = """
Time:      7  15   30
Distance:  9  40  200
        """
    def test_part1(self):
        self.assertEqual(day06.solvePart1(self.lines.splitlines()), 288)
    def test_part2(self):
        self.assertEqual(day06.solvePart2(self.lines.splitlines()), 71503)

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

class Day09(unittest.TestCase):
    def test_part1(self):
        lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
        """
        self.assertEqual(day09.solvePart1(lines.splitlines()), 114)
    def test_part2(self):
        lines = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
        """
        self.assertEqual(day09.solvePart2(lines.splitlines()), 2)
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

class Day11(unittest.TestCase):
    def test_part1(self):
        lines = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
        """
        self.assertEqual(day11.solvePart1(lines.splitlines()), 374)
    def test_part2_1(self):
        lines = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
        """
        self.assertEqual(day11.solve_it(lines.splitlines(), 10), 1030)
    def test_part2_2(self):
        lines = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
        """
        self.assertEqual(day11.solve_it(lines.splitlines(), 100), 8410)

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
    def test_countMatches(self):
        tests = [
("#.#.### 1,1,3", 1),
("???.### 1,1,3", 1),
(".??..??...?##. 1,1,3", 4),
("?#?#?#?#?#?#?#? 1,3,1,6", 1),
("????.#...#... 4,1,1", 1),
("????.######..#####. 1,6,5", 4),
("?###???????? 3,2,1", 10),
                ]
        for test in tests:
            self.assertEqual(day12.countMatches(test[0]), test[1])
    def test_countMatchesUnFolded(self):
        tests = [
("???.### 1,1,3", 1),
(".??..??...?##. 1,1,3", 16384),
("?#?#?#?#?#?#?#? 1,3,1,6", 1),
("????.#...#... 4,1,1", 16),
("????.######..#####. 1,6,5", 2500),
("?###???????? 3,2,1", 506250),
                ]
        for test in tests:
            self.assertEqual(day12.countMatchesUnFolded(test[0]), test[1])
    def test_part2(self):
        lines = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
        self.assertEqual(day12.solvePart2(lines.splitlines()), 525152)

class Day13(unittest.TestCase):
    def test_pattern_score_1(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        self.assertEqual(day13.pattern_score(lines.splitlines(), False), 5)
    def test_pattern_score_2(self):
        lines = """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.pattern_score(lines.splitlines(), True), 100)
    def test_part1(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.solvePart1(lines.splitlines()), 405)
    def test_part2(self):
        lines = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        self.assertEqual(day13.solvePart2(lines.splitlines()), 400)
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

class Day15(unittest.TestCase):
    input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
    def test_part1(self):
        self.assertEqual(day15.solvePart1(self.input.splitlines()), 1320)
    def test_part2(self):
        self.assertEqual(day15.solvePart2(self.input.splitlines()), 145)
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

class Day18(unittest.TestCase):
    lines = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
    def test_part1(self):
        self.assertEqual(day18.solvePart1(self.lines.splitlines()), 62)

    def test_part2(self):
        self.assertEqual(day18.solvePart2(self.lines.splitlines()), 952408144115)

class Day19(unittest.TestCase):
    lines = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
    def test_part1(self):
        self.assertEqual(day19.solvePart1(self.lines.splitlines()), 19114)

    def test_part2(self):
        self.assertEqual(day19.solvePart2(self.lines.splitlines()), 167409079868000)


class Day20(unittest.TestCase):
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
        self.assertEqual(day20.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day20.solvePart2(self.lines.splitlines()), 94)


class Day21(unittest.TestCase):
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
        self.assertEqual(day21.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day21.solvePart2(self.lines.splitlines()), 94)


class Day22(unittest.TestCase):
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
        self.assertEqual(day22.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day22.solvePart2(self.lines.splitlines()), 94)


class Day23(unittest.TestCase):
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
        self.assertEqual(day23.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day23.solvePart2(self.lines.splitlines()), 94)


class Day24(unittest.TestCase):
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
        self.assertEqual(day24.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day24.solvePart2(self.lines.splitlines()), 94)


class Day25(unittest.TestCase):
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
        self.assertEqual(day25.solvePart1(self.lines.splitlines()), 102)

    def test_part2(self):
        self.assertEqual(day25.solvePart2(self.lines.splitlines()), 94)

if __name__ == '__main__':
    unittest.main()