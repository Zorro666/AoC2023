import aoc

"""
"""

def solvePart1(lines):
    result = 0
    for l in lines:
        result += len(l)
    return result

def solvePart2(lines):
    result = 0
    for l in lines:
        result += len(l)
    return result

def main():
    aoc.run_day(16, solvePart1, 123, solvePart2, 456)

if __name__ == '__main__':
    main()