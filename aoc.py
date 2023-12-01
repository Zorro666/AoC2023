import time

import day01
import day02
import day03

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
