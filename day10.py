import aoc

"""
--- Day 10: Pipe Maze ---
You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island.
This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

You wander around for a while, but you don't find any people or animals.
However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal.
As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground".
You make a quick sketch of all of the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.

S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF

In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on.
Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position.
Because the animal is in the pipe, it doesn't make sense to measure this by direct distance.
Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S.
How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

Your puzzle answer was 6864.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You quickly reach the farthest point of the loop, but the animal never emerges.
Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop.
For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below).
The middle . tiles (marked O below) are not in the loop.
Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

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
The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the loop.
Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

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
Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the area within the loop.
How many tiles are enclosed by the loop?
"""

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# pipes connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on.
# Every pipe in the main loop connects to its two neighbors

grid = []
loop = []
cells = []
width = 0
height = 0

def find_loop(lines):
    grid.clear()
    grid.append(".")
    width = 0
    for l in lines:
        if l.strip() == '':
            continue
        row = '.' + l.strip() + '.'
        grid.append(row)
        width = max(width, len(row))

    grid[0] = '.'*width
    grid.append(grid[0])
    height = len(grid)

    startX = 0
    startY = 0
    for y in range(1, height-1):
        for x in range(1, width-1):
            c = grid[y][x]
            if c == 'S':
                startX = x
                startY = y
                break
    
    # Follow the pipe from start
    x = startX
    y = startY
    n = grid[y-1][x]
    w = grid[y][x-1]
    e = grid[y][x+1]
    s = grid[y+1][x]
    northValid = (n == '|' or n == '7' or n == 'F' or n == 'S')
    southValid = (s == '|' or s == 'L' or s == 'J' or s == 'S')
    westValid = (w == '-' or w == 'L' or w == 'F' or w == 'S')
    eastValid = (e == '-' or e == '7' or e == 'J' or e == 'S')
    nextMove = '.'

    # Replace the start with the correct character
    startC = 'S'
    if northValid and southValid and not westValid and not eastValid:
        startC = '|'
    elif not northValid and not southValid and westValid and eastValid:
        startC = '-'
    elif northValid and not southValid and not westValid and eastValid:
        startC = 'L'
    elif northValid and not southValid and westValid and not eastValid:
        startC = 'J'
    elif not northValid and southValid and not westValid and eastValid:
        startC = 'F'
    elif not northValid and southValid and westValid and not eastValid:
        startC = '7'
    grid[startY] = grid[startY].replace('S', startC)

    if westValid:
        nextMove = 'w'
    elif northValid:
        nextMove = 'n'
    elif eastValid:
        nextMove = 'e'
    elif southValid:
        nextMove = 's'

    lastMove = '.'
    loop.clear()
    loop.append((x,y))
    while True:
        newX = x
        newY = y
        n = grid[y-1][x]
        w = grid[y][x-1]
        e = grid[y][x+1]
        s = grid[y+1][x]
        northValid = (n == '|' or n == '7' or n == 'F')
        southValid = (s == '|' or s == 'L' or s == 'J')
        westValid = (w == '-' or w == 'L' or w == 'F')
        eastValid = (e == '-' or e == '7' or e == 'J')
        if nextMove == 'n' and not northValid:
            exit("Bad move:" + nextMove)
        elif nextMove == 's' and not southValid:
            exit("Bad move:" + nextMove)
        elif nextMove == 'w' and not westValid:
            exit("Bad move:" + nextMove)
        elif nextMove == 'e' and not eastValid:
            exit("Bad move:" + nextMove)

        if nextMove == 'w':
            newX = x-1
            lastMove = 'w'
        elif nextMove == 'n':
            newY = y-1
            lastMove = 'n'
        elif nextMove == 'e':
            newX = x+1
            lastMove = 'e'
        elif nextMove == 's':
            newY = y+1
            lastMove = 's'
        else:
            exit("No valid moves")

        x = newX
        y = newY
        c = grid[y][x]
        if x == startX and y == startY:
            break
        if c == '|':
            if lastMove == 'n':
                nextMove = 'n'
            elif lastMove == 's':
                nextMove = 's'
            else:
                exit("Bad last move")
        elif c == '-':
            if lastMove == 'w':
                nextMove = 'w'
            elif lastMove == 'e':
                nextMove = 'e'
            else:
                exit("Bad last move")
        elif c == '7':
            if lastMove == 'n':
                nextMove = 'w'
            elif lastMove == 'e':
                nextMove = 's'
            else:
                exit("Bad last move")
        elif c == 'F':
            if lastMove == 'n':
                nextMove = 'e'
            elif lastMove == 'w':
                nextMove = 's'
            else:
                exit("Bad last move")
        elif c == 'L':
            if lastMove == 'w':
                nextMove = 'n'
            elif lastMove == 's':
                nextMove = 'e'
            else:
                exit("Bad last move")
        elif c == 'J':
            if lastMove == 's':
                nextMove = 'w'
            elif lastMove == 'e':
                nextMove = 'n'
            else:
                exit("Bad last move")

        loop.append((x,y))

def flood_fill(x, y):
    nodes = []
    nodes.append((x,y))
    while len(nodes) > 0:
        n = nodes.pop()
        x = n[0]
        y = n[1]
        if cells[y][x] == 1 or cells[y][x] == 3:
            continue
        cells[y][x] = 3
        if y > 0:
            nodes.append((x, y-1))
        if y < height-1:
            nodes.append((x, y+1))
        if x > 0:
            nodes.append((x-1, y))
        if x < width-1:
            nodes.append((x+1, y))

def inside(x, y):
    # Horizontally an edge is:
    # | , FJ , L7 
    # ignore '-' between FJ L7
    # F7 : is not an edge
    # LJ : is not an edge

    # Vertically an edge is:
    # -, F , 7
    #    J , L
    # ignore '|' between FJ 7L
    # F : is not an edge
    # L
    # 7 : is not an edge
    # J
    edges = 0
    lastC = '.'
    for i in range(0, x):
        if cells[y][i] == 1:
            c = grid[y][i]
            if c == '-':
                continue
            if c == 'S':
                exit("oh no")
            if c == '|':
                edges += 1
            elif (lastC == 'F' and c == 'J'):
                edges += 1
            elif (lastC == 'L' and c == '7'):
                edges += 1
            lastC = c

    if edges % 2 == 0:
        return False

    edges = 0
    lastC = '.'
    for i in range(x+1, width):
        if cells[y][i] == 1:
            c = grid[y][i]
            if c == 'S':
                exit("oh no")
            if c == '-':
                continue
            if c == '|':
                edges += 1
            elif (lastC == 'F' and c == 'J'):
                edges += 1
            elif (lastC == 'L' and c == '7'):
                edges += 1
            lastC = c

    if edges % 2 == 0:
        return False

    edges = 0
    lastC = '.'
    for j in range(0, y):
        if cells[j][x] == 1:
            c = grid[j][x]
            if c == 'S':
                exit("oh no")
            if c == '|':
                continue
            if c == '-':
                edges += 1
            elif (lastC == 'F' and c == 'J'):
                edges += 1
            elif (lastC == '7' and c == 'L'):
                edges += 1
            lastC = c

    if edges % 2 == 0:
        return False

    edges = 0
    lastC = '.'
    for j in range(y+1, height):
        if cells[j][x] == 1:
            c = grid[j][x]
            if c == 'S':
                exit("oh no")
            if c == '|':
                continue
            if c == '-':
                edges += 1
            elif (lastC == 'F' and c == 'J'):
                edges += 1
            elif (lastC == '7' and c == 'L'):
                edges += 1
            lastC = c

    if edges % 2 == 0:
        return False

    return True

def solvePart1(lines):
    find_loop(lines)
    distsA = {}
    distsB = {}
    for i in range(1, len(loop)):
        path1 = loop[i]
        path2 = loop[len(loop)-i]
        distsA[path1] = i
        distsB[path2] = i

    dist = 0
    for p in distsA:
        d = min(distsA[p], distsB[p])
        dist = max(dist,d)

    return dist

def solvePart2(lines):
    find_loop(lines)

    global width
    global height
    width = len(grid[0])
    height = len(grid)
    cells.clear()
    minYs = []
    maxYs = []
    minXs = []
    maxXs = []
    for y in range(height):
        row = []
        minXs.append(height)
        maxXs.append(0)
        for x in range(width):
            minYs.append(width)
            maxYs.append(0)
            row.append(0)
        cells.append(row)

    for i in range(0, len(loop)):
        xy = loop[i]
        x = xy[0]
        y = xy[1]
        cells[y][x] = 1
        minYs[x] = min(minYs[x], y)
        maxYs[x] = max(maxYs[x], y)
        minXs[y] = min(minXs[y], x)
        maxXs[y] = max(maxXs[y], x)

    for y in range(height):
        for x in range(width):
            if cells[y][x] == 0:
                if y > minYs[x] and y < maxYs[x] and x > minXs[y] and x < maxXs[y]:
                    cells[y][x] = 2

    # Not required but looks pretty
    # Flood fill from 0,0 with 3 except cells of 1
    flood_fill(0,0)

    # For each cell of value 2 count the edges to left, right, up, down
    # Even edges means outside
    result = 0
    for y in range(height):
        for x in range(width):
            if cells[y][x] == 2:
                if inside(x,y):
                    result += 1

    return result

def main():
    aoc.run_day(10, solvePart1, 6864, solvePart2, 349)

if __name__ == '__main__':
    main()