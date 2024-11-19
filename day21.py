import aoc
from collections import deque

"""
--- Day 21: Step Counter ---

You manage to catch the airship right as it's dropping someone else off on their all-expenses-paid trip to Desert Island!
It even helpfully drops you off near the gardener and his massive farm.

"You got the sand flowing again!
Great work!
Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."

While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help.
He needs to get his steps in for the day, and so he'd like to know which garden plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#).

For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

The Elf starts at the starting position (S) which also counts as a garden plot.

Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots.

This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........

Then, he takes a second step.

Since at this point he could be at either tile marked O, his second step would allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........

After two steps, he could be at any of the tiles marked O above, including the starting position (either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........

He will continue like this until his steps for the day have been exhausted.

After a total of 6 steps, he could reach any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........

In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?

--- Part Two ---

The Elf seems confused by your answer until he realizes his mistake:
he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.

The actual number of steps he needs to get today is exactly 26501365.

He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.

So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................

This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout;
garden plots and rocks repeat as far as you can see.
The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).

Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

In exactly 6 steps, he can still reach 16 garden plots.
In exactly 10 steps, he can reach any of 50 garden plots.
In exactly 50 steps, he can reach 1594 garden plots.
In exactly 100 steps, he can reach 6536 garden plots.
In exactly 500 steps, he can reach 167004 garden plots.
In exactly 1000 steps, he can reach 668697 garden plots.
In exactly 5000 steps, he can reach 16733044 garden plots.

However, the step count the Elf needs is much larger!
Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?

"""

'''
26501365 is target
Its factors are: 1, 5, 11, 55, 481843, 2409215, 5300273, 26501365
The grid is 131 x 131
Start is 65, 65

(26501365 - 65) % 131 = 0

Grid_Size = 131

Compute number of locations in infinite grid at step counts of:

65, 65 + 131, 65 + 131 * 2

The number of locations in steps to the mid-points of grids in the infinite grid 
is a quadratic function of the grid count.

loc(grid_size) = a * grid_size^2 + b * grid_size + c

a + b + c = loc(1)    => a + b = loc(1) - loc(0)
4a + 2b + c = loc(2)  => 4a + 2b = loc(2) - loc(0)

2a = loc(2) - loc(0) - 2 * (loc(1) - loc(0)) => 

a = (loc(2) - 2 * loc(1) + loc(0))/2
b = loc(1) - loc(0) - a
c = loc(0)

Get loc(65, 65+131, 65 * 131*2)

'''

def parse(lines):
    grid = []
    for l in lines:
        l = l.strip()
        if len(l) == 0:
            continue
        if 'S' in l:
            x = l.index('S')
            y = len(grid)
            startPos = (x, y)
        grid.append(list(l))

    grid[startPos[1]][startPos[0]] = '.'
    return grid, startPos

def countLocations(lines, maxSteps):
    grid, startPos = parse(lines)
    h = len(grid)
    w = len(grid[0])
    locations = deque()
    locations.append(startPos)
    visited = {startPos: 0}
    results = []

    step = 0
    maxStep = max(maxSteps)
    while step < maxStep:
        step += 1
        newLocations = deque()
        while locations:
            (x, y) = locations.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                gx = nx % w
                gy = ny % h
                if grid[gy][gx] == '.' and (nx, ny) not in visited:
                    newLocations.append((nx, ny))
                    visited[(nx, ny)] = step
        locations = newLocations
        if step in maxSteps:
            results.append(len([d for d in visited.values() if d % 2 == step % 2]))

    return results

def solvePart1(lines):
    return countLocations(lines, [64])[0]

def solvePart2(lines):
    numSamples = 4
    maxSteps = []
    for i in range(numSamples):
        maxSteps.append(65 + 131 * i)
    locs = countLocations(lines, maxSteps)
    #a = (loc(2) - 2 * loc(1) + loc(0))/2
    #b = loc(1) - loc(0) - a
    #c = loc(0)
    a = (locs[2] - 2 * locs[1] + locs[0]) // 2
    b = locs[1] - locs[0] - a
    c = locs[0]

    # Check the quadratic equation fits
    for i in range(numSamples):
        if locs[i] != a * i * i + b * i + c:
            print(f'Error in calculation at {i} {locs[i]} != {a * i * i + b * i + c}')
            return 0

    N = 26501365 
    grids = (N - 65)//131
    result = a * grids * grids + b * grids + c
    return result

def main():
    aoc.run_day(21, solvePart1, 3562, solvePart2, 592723929260582)

if __name__ == '__main__':
    main()