import aoc

"""
--- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water.
Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days...weeks...oh no." 
His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat.
Could you please go check it out?"

You barely have time to agree to this request when he brings up another.
"While you wait for the ferry, maybe you can help us with our food production problem.
The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted.
It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on.
Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category.
That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination).
This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted.
Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2.
This line means that the source range starts at 98 and contains two values: 98 and 99.
The destination range is the same length, but it starts at 50, so its two values are 50 and 51.
With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97.
This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99.
So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number.
So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed.
Using these maps, find the lowest location number that corresponds to any of the initial seeds.
To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number.
In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

To begin, get your puzzle input.

Your puzzle answer was 107430936.

--- Part Two ---

Everyone will starve if you only plant such a small number of seeds.
Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs.
Within each pair, the first value is the start of the range and the second value is the length of the range.
So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden.
The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92.
The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46.
So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac.
What is the lowest location number that corresponds to any of the initial seed numbers?

"""

def solvePart1(lines):
    seeds = []
    conversions_src_start = []
    conversions_dst_start = []
    conversions_count = []
    conversion_index = -1
    for l in lines:
        #seeds: 79 14 55 13
        l = l.strip()
        if l.startswith("seeds: "):
            seeds = [int(x) for x in l[7:].split()]
            continue
        #seed-to-soil map:
        #soil-to-fertilizer map:
        #fertilizer-to-water map:
        #water-to-light map:
        #light-to-temperature map:
        #temperature-to-humidity map:
        #humidity-to-location map:
        if l.endswith(" map:"):
            conversions_src_start.append([])
            conversions_dst_start.append([])
            conversions_count.append([])
            continue
        if l.strip() == "":
            conversion_index += 1
            continue
        # 45 77 23
        values = l.split()
        conversions_dst_start[conversion_index].append(int(values[0]))
        conversions_src_start[conversion_index].append(int(values[1]))
        conversions_count[conversion_index].append(int(values[2]))
    result = 999999999999999999999
    for seed in seeds:
        for i in range(len(conversions_src_start)):
            for j in range(len(conversions_src_start[i])):
                if seed >= conversions_src_start[i][j] and seed < conversions_src_start[i][j] + conversions_count[i][j]:
                    seed = conversions_dst_start[i][j] + seed - conversions_src_start[i][j]
                    break
        result = min(result, seed)
    return result

def solvePart2(lines):
    seeds = []
    conversions_src_start = []
    conversions_dst_start = []
    conversions_count = []
    conversion_index = -1
    for l in lines:
        #seeds: 79 14 55 13
        l = l.strip()
        if l.startswith("seeds: "):
            seeds = [int(x) for x in l[7:].split()]
            continue
        #seed-to-soil map:
        #soil-to-fertilizer map:
        #fertilizer-to-water map:
        #water-to-light map:
        #light-to-temperature map:
        #temperature-to-humidity map:
        #humidity-to-location map:
        if l.endswith(" map:"):
            conversions_src_start.append([])
            conversions_dst_start.append([])
            conversions_count.append([])
            continue
        if l.strip() == "":
            conversion_index += 1
            continue
        # 45 77 23
        values = l.split()
        conversions_dst_start[conversion_index].append(int(values[0]))
        conversions_src_start[conversion_index].append(int(values[1]))
        conversions_count[conversion_index].append(int(values[2]))

    # Sort the conversion ranges by start lowest->highest
    for i in range(len(conversions_src_start)):
        for j in range(len(conversions_src_start[i])-1):
            for k in range(j+1, len(conversions_src_start[i])):
                if (conversions_src_start[i][k] < conversions_src_start[i][j]):
                    temp = conversions_src_start[i][j]
                    conversions_src_start[i][j] = conversions_src_start[i][k]
                    conversions_src_start[i][k] = temp
                    temp =conversions_dst_start[i][j]
                    conversions_dst_start[i][j] = conversions_dst_start[i][k]
                    conversions_dst_start[i][k] = temp
                    temp =conversions_count[i][j]
                    conversions_count[i][j] = conversions_count[i][k]
                    conversions_count[i][k] = temp

    result = 999999999999
    ranges = []
    # All ranges are inclusive start, end
    for s in range(0, len(seeds), 2):
        range_start = seeds[s]
        range_end = range_start + seeds[s+1] - 1
        ranges.append((range_start, range_end))

    for i in range(len(conversions_src_start)):
        new_ranges = []
        for r in ranges:
            rs = r[0]
            re = r[1]
            if re < rs:
                continue
            
            for k in range(len(conversions_src_start[i])):
                if re < rs:
                    break
                cs = conversions_src_start[i][k]
                ce = conversions_src_start[i][k] + conversions_count[i][k] -1
                delta = conversions_dst_start[i][k] - conversions_src_start[i][k]

                # Remove all overlapping pieces from the range to start with
                # Ranges are sorted by their start value from smallest to largest
                # Any value within cs->ce must be transformed when making the new range

                # No overlap
                # rs--re
                #         cs-----ce
                # rs--re
                if re < cs:
                    break
                #
                #              rs--re
                # cs-----ce
                #              rs--re
                if rs > ce:
                   continue
                #     rs------re
                # cs---------------ce
                #     rs*-----re*
                elif rs >= cs and re <= ce:
                    new_ranges.append((rs+delta,re+delta))
                    rs = 0
                    re = -1
                    break
                # rs-------------re
                #     cs-----ce
                # rs--cs
                #     cs*----ce*
                #            ce--re
                elif rs <= cs and re >= ce:
                    new_ranges.append((cs+delta,ce+delta))
                    new_ranges.append((rs,cs-1))
                    rs = ce+1
                # rs------re
                #     cs-----ce
                # rs--cs
                #     cs*-re*
                elif rs <= cs and re <= ce:
                    new_ranges.append((cs+delta,re+delta))
                    re = cs-1
                #     rs-------re
                # cs------ce
                #     rs*-ce*
                #         ce---re
                elif rs >= cs and re >= ce:
                    new_ranges.append((rs+delta,ce+delta))
                    rs = ce+1
                else:
                    print("unhandled range overlap")
            if re >= rs:
                new_ranges.append((rs,re))
        # Could merge ranges but don't need to
        ranges = new_ranges

    for r in ranges:
        result = min(r[0], result)
    return result

def main():
    aoc.run_day(5, solvePart1, 107430936, solvePart2, 23738616)

if __name__ == '__main__':
    main()