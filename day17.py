import aoc
import queue

"""
--- Day 17: Clumsy Crucible ---

The lava starts flowing rapidly once the Lava Production Facility is operational.
As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.

As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: 
half of Gear Island is empty, but the half below you is a giant factory city!

You land near the gradually-filling pool of lava at the base of your new lavafall.
Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.

The crucibles are top-heavy and pushed by hand.
Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.

To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory.
To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

For example:

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

Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block.
The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block.
(Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right.
The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:

2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?

-- Part Two ---
The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory.
Instead, the Elves are going to upgrade to ultra crucibles.

Ultra crucibles are even more difficult to steer than normal crucibles.
Not only do they have trouble going in a straight line, but they also have trouble turning!

Once an ultra crucible starts moving in a direction, it needs to move a minimum of four blocks in that direction before it can turn (or even before it can stop at the end).
However, it will eventually start to get wobbly: an ultra crucible can move a maximum of ten consecutive blocks without turning.

In the above example, an ultra crucible could follow this path to minimize heat loss:

2>>>>>>>>1323
32154535v5623
32552456v4254
34465858v5452
45466578v>>>>
143859879845v
445787698776v
363787797965v
465496798688v
456467998645v
122468686556v
254654888773v
432267465553v
In the above example, an ultra crucible would incur the minimum possible heat loss of 94.

Here's another example:

111111111111
999999999991
999999999991
999999999991
999999999991
Sadly, an ultra crucible would need to take an unfortunate path like this one:

1>>>>>>>1111
9999999v9991
9999999v9991
9999999v9991
9999999v>>>>
This route causes the ultra crucible to incur the minimum possible heat loss of 71.

Directing the ultra crucible from the lava pool to the machine parts factory, what is the least heat loss it can incur?

"""

GO_LEFT = 0
GO_RIGHT = 1
GO_UP = 2
GO_DOWN = 3

h = 0
w = 0
grid = []
visited: set[tuple[int,int,int,int]] = set()

def parse(lines):
    global h, w, grid, minHeatsPerDir
    grid.clear()
    visited.clear()
    for l in lines:
        l = l.strip()
        if len(l) == 0:
            continue
        line = []
        for c in l:
            line.append(int(c))
        grid.append(line)
    h = len(grid)
    w = len(grid[0])

def solve(lines, min_steps, max_steps):
    global h, w, grid, minHeats
    parse(lines)

    startingPoints = queue.PriorityQueue()
    x = 0
    y = 0
    heat = 0
    minHeat = 999999999
    startingPoints.put((heat, x, y, GO_RIGHT, 0))
    startingPoints.put((heat, x, y, GO_DOWN, 0))

    while not startingPoints.empty():
        current = startingPoints.get()
        heat = current[0]
        x = current[1]
        y = current[2]
        direction = current[3]
        steps = current[4]
        if x == w-1 and y == h-1 and steps >= min_steps:
            if heat < minHeat:
                print(f'New min heat: {heat}')
                minHeat = heat
            continue
        if heat >= minHeat:
            continue
        new_visit = (x,y,direction,steps)
        if new_visit in visited:
            continue
        visited.add(new_visit)

#        print(f'x: {x}, y: {y}, heat: {heat}, direction: {direction}, steps: {steps}')
        # Move one forward
        # Rotate Left and move one
        # Rotate Right and move one
        new_moves = []
        if direction == GO_LEFT:
            new_moves.append((GO_LEFT, x-1, y, steps+1))
            if steps >= min_steps:
                new_moves.append((GO_UP, x, y-1, 1))
                new_moves.append((GO_DOWN, x, y+1, 1))
        elif direction == GO_RIGHT:
            new_moves.append((GO_RIGHT, x+1, y, steps+1))
            if steps >= min_steps:
                new_moves.append((GO_UP, x, y-1, 1))
                new_moves.append((GO_DOWN, x, y+1, 1))
        elif direction == GO_UP:
            new_moves.append((GO_UP, x, y-1, steps+1))
            if steps >= min_steps:
                new_moves.append((GO_LEFT, x-1, y, 1))
                new_moves.append((GO_RIGHT, x+1, y, 1))
        elif direction == GO_DOWN:
            new_moves.append((GO_DOWN, x, y+1, steps+1))
            if steps >= min_steps:
                new_moves.append((GO_LEFT, x-1, y, 1))
                new_moves.append((GO_RIGHT, x+1, y, 1))
        
        for move in new_moves:
            new_x = move[1]
            new_y = move[2]
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            new_steps = move[3]
            if new_steps > max_steps:
                continue
            new_direction = move[0]
            new_heat = heat + grid[new_y][new_x]
            startingPoints.put((new_heat, new_x, new_y, new_direction, new_steps))

    return minHeat

def solvePart1(lines):
    return solve(lines, 0, 3)

def solvePart2(lines):
    return solve(lines, 4, 10)

def main():
    aoc.run_day(17, solvePart1, 665, solvePart2, 809)

if __name__ == '__main__':
    main()