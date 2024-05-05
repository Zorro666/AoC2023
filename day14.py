import aoc
import copy

"""
--- Day 14: Parabolic Reflector Dish ---

You reach the place where all of the mirrors were pointing: 
a massive parabolic reflector dish attached to the side of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction.
If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish.
The platform is covered in large rocks of various shapes.
Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish.
The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place.
You note the positions of all of the empty spaces (.) and rocks (your puzzle input).
For example:

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
Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
You notice that the support beams along the north side of the platform are damaged; 
to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on.
(Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1

The total load is the sum of the load caused by all of the rounded rocks.
In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north.
Afterward, what is the total load on the north support beams?

--- Part Two ---

The parabolic reflector dish deforms, but not in a way that focuses the beam.
To do that, you'll need to move the rocks to the edges of the platform.
Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east.
After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction.
After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
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

After 2 cycles:
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

After 3 cycles:
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

This process should work if you leave it running long enough, but you're still worried about the north support beams.
To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

Run the spin cycle for 1000000000 cycles.
Afterward, what is the total load on the north support beams?
"""

def parse(lines):
    grid = []
    w = 0
    h = 0
    for l in lines:
        l = l.strip()
        if len(l) == 0:
            continue
        if w == 0:
            w = len(l)
        if w != len(l):
            raise Exception("invalid input")
        grid.append(list(l))
        h +=1

    for y in range(int(h/2)):
        yFlip = h - y - 1
        t = grid[yFlip]
        grid[yFlip] = grid[y]
        grid[y] = t
    return (grid, w, h)

def rollNorth(grid, w, h):
    y = h - 2
    while y >= 0:
        for x in range(w):
            if grid[y][x] == 'O':
                y2 = y + 1
                while y2 < h and grid[y2][x] == '.':
                    y2 += 1
                y2 -= 1
                if y != y2:
                    grid[y][x] = '.'
                    grid[y2][x] = 'O'
        y -= 1

def rollSouth(grid, w, h):
    y = 1
    while y < h:
        for x in range(w):
            if grid[y][x] == 'O':
                y2 = y - 1
                while y2 >= 0 and grid[y2][x] == '.':
                    y2 -= 1
                y2 += 1
                if y != y2:
                    grid[y][x] = '.'
                    grid[y2][x] = 'O'
        y += 1

def rollWest(grid, w, h):
    x = 1
    while x < w:
        for y in range(h):
            if grid[y][x] == 'O':
                x2 = x - 1
                while x2 >= 0 and grid[y][x2] == '.':
                    x2 -= 1
                x2 += 1
                if x != x2:
                    grid[y][x] = '.'
                    grid[y][x2] = 'O'
        x += 1

def rollEast(grid, w, h):
    x = w - 2
    while x >= 0:
        for y in range(h):
            if grid[y][x] == 'O':
                x2 = x + 1
                while x2 < w and grid[y][x2] == '.':
                    x2 += 1
                x2 -= 1
                if x != x2:
                    grid[y][x] = '.'
                    grid[y][x2] = 'O'
        x -= 1

def scoreGrid(grid, w, h):
    score = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'O':
                score += (y+1)
    return score

def runCycle(grid, w, h):
    rollNorth(grid, w, h)
    rollWest(grid, w, h)
    rollSouth(grid, w, h)
    rollEast(grid, w, h)

def solvePart1(lines):
    (grid, w, h) = parse(lines)
    rollNorth(grid, w, h)
    return scoreGrid(grid, w, h)

def solvePart2(lines):
    (grid, w, h) = parse(lines)
    cycle = 0
    testCycles = 1000
    grids = []
    # Find the cycle : Intro Count + N * Cycles + Remainder
    start = -1
    period = -1
    while cycle < testCycles:
        runCycle(grid, w, h)
        i = 0
        idx = -1
        while i < len(grids):
            if grids[i] == grid:
                idx = i
                break
            i += 1
        if idx != -1:
            if start == -1:
                start = cycle
                period = -1
            elif period == -1:
                period = cycle - idx
                break
        grids.append(copy.deepcopy(grid))
        cycle += 1

    totalCycles = 1000000000
    grid = grids[start-1]
    remainingCycles = (totalCycles - start) % period
    for i in range(remainingCycles):
        runCycle(grid, w, h)

    print(f"Cycle Start: {start} Period: {period} Remaining: {remainingCycles}")
    return scoreGrid(grid, w, h)

def main():
    aoc.run_day(14, solvePart1, 109596, solvePart2, 96105)

if __name__ == '__main__':
    main()