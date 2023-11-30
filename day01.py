import aoc

def increment(x):
    return x + 1

def decrement(x):
    return x - 1

def solvePart1(lines):
    for l in lines:
        for w in l.split():
            print(w)

def solvePart2(lines):
    for l in lines:
        ws = l.split()

def part1():
    lines = aoc.parse("day01.txt")
    solvePart1(lines)

def part2():
    lines = aoc.parse("day01.txt")
    solvePart2(lines);

if __name__ == '__main__':
    aoc.run(1, 1, part1)
    aoc.run(1, 2, part2)