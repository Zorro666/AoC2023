import aoc

"""
--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an observatory.
The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project.
However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input).
The image includes empty space (.) and galaxies (#).
For example:

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
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies.
However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands.
In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found.
It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

In these 9 galaxies, there are 36 pairs.
Only count each pair once; order within the pair doesn't matter.
For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time.
(The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......

This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself).
Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?

Number of pairs = n! / k!(n-k)! : n = countGalaxy, k = 2
Number of pairs = countGalaxy * (countGalaxy-1) / 2

Your puzzle answer was 9177603.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger.
That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030.
If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410.
However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?
"""

def solve_it(lines, expand):
    cells = []
    emptyRows = []
    for l in lines:
        if l.strip() == '':
            continue
        row = []
        emptyRow = True
        for c in l.strip():
            if c == '.':
                row.append(0)
            elif c == '#':
                row.append(1)
                emptyRow = False
            else:
                exit("Bad char")
        cells.append(row)
        emptyRows.append(emptyRow)

    height = len(cells)
    width = len(cells[0])
    emptyCols = []
    for x in range(width):
        emptyCol = True
        for y in range(height):
            if cells[y][x] == 1:
                emptyCol = False
                break
        emptyCols.append(emptyCol)

    height = len(cells)
    width = len(cells[0])
    galaxys = []
    for y in range(height):
        for x in range(width):
            if cells[y][x] == 1:
                galaxys.append((x,y))

    result = 0
    for i in range(len(galaxys)):
        g1 = galaxys[i]
        for j in range(i+1, len(galaxys)):
            g2 = galaxys[j]
            if g1 == g2:
                continue
            g1_x = g1[0]
            g1_y = g1[1]
            g2_x = g2[0]
            g2_y = g2[1]
            dx = abs(g2_x - g1_x)
            dy = abs(g2_y - g1_y)
            d = abs(dx) + abs(dy)

            for x in range(min(g1_x, g2_x), max(g1_x, g2_x)):
                if emptyCols[x]:
                    d += expand-1
            for y in range(min(g1_y, g2_y), max(g1_y, g2_y)):
                if emptyRows[y]:
                    d += expand-1
            result += d

    return result

def solvePart1(lines):
    return solve_it(lines, 2)

def solvePart2(lines):
    return solve_it(lines, 1000000)

def main():
    aoc.run_day(11, solvePart1, 9177603, solvePart2, 632003913611)

if __name__ == '__main__':
    main()