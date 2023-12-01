import time

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

def parse(fname):
    with open(fname, "r") as file:
        return file.readlines()

def run_day(day, part1, expected1, part2, expected2):
    print("Day{:d}: Start".format(day))
    lines = parse("day{:02d}.txt".format(day))
    start = time.time()

    result1 = part1(lines)
    print("Day{}: Result1 {}".format(day, result1))
    if result1 != expected1:
        print("Part1 is broken {} != {}".format(result1, expected1))
        quit()

    result2 = part2(lines);
    print("Day{}: Result2 {}".format(day, result2))
    if result2 != expected2:
        print("Part2 is broken {} != {}".format(result2, expected2))
        quit()

    end = time.time()
    dt = end - start
    seconds = dt
    mins = seconds / 60.0
    ms = int(seconds * 1000)
    print("Day{:d}: End Elapsed {:d}ms {:.2f}s {:.1f}mins".format(day, ms, seconds, mins))

if __name__ == '__main__':
    day01.main()
    day02.main()
    day03.main()
    day04.main()
    day05.main()
    day06.main()
    day07.main()
    day08.main()
    day09.main()
    day10.main()
    day11.main()
    day12.main()
    day13.main()
    day14.main()
    day15.main()
    day16.main()
    day17.main()
    day18.main()
    day19.main()
    day20.main()
    day21.main()
    day22.main()
    day23.main()
    day24.main()
    day25.main()