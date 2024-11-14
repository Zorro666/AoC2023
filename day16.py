import aoc

'''
--- Day 16: The Floor Will Be Lava ---
With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility.
At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead.
There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input).
For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\..
.-.-/..|..
.|....-|.\\
..//.|....
The beam enters in the top-left corner from the left and heading to the right.
Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.

If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror.
For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.

If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space.
For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.

If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing.
For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

Beams do not interact with other beams; a tile can have many beams passing through it at the same time.
A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\\
.v../2\\..
<->-/vv|..
.|<<<2-|.\\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams.
If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead.
Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..

Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation.
With the beam starting in the top-left heading right, how many tiles end up being energized?

--- Part Two ---

As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel.
There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge.
(You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left).
To produce lava, you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..

Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
'''

RAY_EMPTY = 0
RAY_LEFT = 1
RAY_RIGHT = 2
RAY_UP = 4
RAY_DOWN = 8

def countEnergized(start, grid, w, h):
    rays = []
    rays.append(start)

    light = []
    for i in range(h):
        light.append([RAY_EMPTY] * w)

    while (len(rays) > 0):
        ray = rays.pop()
        # Extract x,y from ray tuple (x,y,dx,dy,dir)
        x = ray[0]
        y = ray[1]
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        dx = ray[2]
        dy = ray[3]
        dir = ray[4]
        if light[y][x] & dir == dir:
            continue
        while (light[y][x] & dir != dir):
            light[y][x] |= dir
            cell = grid[y][x]

            if cell != '.':
                if cell == '|':
                    if dx != 0:
                        # Spawn a new beam going up
                        rays.append((x, y-1, 0, -1, RAY_UP))
                        # Reflect beam down
                        dx = 0
                        dy = 1
                        dir = RAY_DOWN
                elif cell == '-':
                    # Split into two beams
                    if dy != 0:
                        # Spawn a new beam going left
                        rays.append((x-1, y, -1, 0, RAY_LEFT))
                        # Reflect beam right
                        dx = 1
                        dy = 0
                        dir = RAY_RIGHT
                elif cell == '\\':
                    # Reflect the beam
                    if dir == RAY_RIGHT:
                        dir = RAY_DOWN
                        dx = 0
                        dy = 1
                    elif dir == RAY_LEFT:
                        dir = RAY_UP
                        dx = 0
                        dy = -1
                    elif dir == RAY_UP:
                        dir = RAY_LEFT
                        dx = -1
                        dy = 0
                    elif dir == RAY_DOWN:
                        dir = RAY_RIGHT
                        dx = 1
                        dy = 0
                elif cell == '/':
                    # Reflect the beam
                    if dir == RAY_LEFT:
                        dir = RAY_DOWN
                        dx = 0
                        dy = 1
                    elif dir == RAY_RIGHT:
                        dir = RAY_UP
                        dx = 0
                        dy = -1
                    elif dir == RAY_DOWN:
                        dir = RAY_LEFT
                        dx = -1
                        dy = 0
                    elif dir == RAY_UP:
                        dir = RAY_RIGHT
                        dx = 1
                        dy = 0

            x += dx
            y += dy
            if x < 0 or x >= w or y < 0 or y >= h:
                break

    result = 0
    for y in range(h):
        for x in range(w):
            if light[y][x] != RAY_EMPTY:
                result += 1
    return result

# Rays : x,y,dx,dy
def solvePart1(lines):
    start = (0,0, 1, 0, RAY_RIGHT)
    grid = []
    for l in lines:
        l = l.strip()
        if len(l) == 0:
            continue
        grid.append(list(l))

    h = len(grid)
    w = len(grid[0])
    return countEnergized(start, grid, w, h)

def solvePart2(lines):
    grid = []
    for l in lines:
        l = l.strip()
        if len(l) == 0:
            continue
        grid.append(list(l))

    w = len(grid[0])
    h = len(grid)
    maxResult = 0
    for x in range(w):
        start = (x,0,0,1, RAY_DOWN)
        result = countEnergized(start, grid, w, h)
        if result > maxResult:
            maxResult = result
        start = (x,h-1,0,-1, RAY_UP)
        result = countEnergized(start, grid, w, h)
        if result > maxResult:
            maxResult = result

    for y in range(h):
        start = (0,y,1,0, RAY_RIGHT)
        result = countEnergized(start, grid, w, h)
        if result > maxResult:
            maxResult = result
        start = (w-1,y,-1,0, RAY_LEFT)
        result = countEnergized(start, grid, w, h)
        if result > maxResult:
            maxResult = result

    return maxResult

def main():
    aoc.run_day(16, solvePart1, 7860, solvePart2, 8331)

if __name__ == '__main__':
    main()