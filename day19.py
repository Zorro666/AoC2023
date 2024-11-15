import aoc
import math

"""
--- Day 19: Aplenty ---
The Elves of Gear Island are thankful for your help and send you on your way.
They even have a hang glider that someone stole from Desert Island; since you're already going that direction, it would help them a lot if you would use it to get down there and return it to them.

As you reach the bottom of the relentless avalanche of machine parts, you discover that they're already forming a formidable heap.
Don't worry, though - a group of Elves is already here organizing the parts, and they have a system.

To start, each part is rated in each of four categories:

x: Extremely cool looking
m: Musical (it makes a noise when you hit it)
a: Aerodynamic
s: Shiny
Then, each part is sent through a series of workflows that will ultimately accept or reject the part.
Each workflow has a name and contains a list of rules; each rule specifies a condition and where to send the part if the condition is true.
The first rule that matches the part being considered is applied immediately, and the part moves on to the destination described by the rule.
(The last rule in each workflow has no condition and always applies if reached.)

Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}.
This workflow is named ex and contains four rules.
If workflow ex were considering a specific part, it would perform the following steps in order:

Rule "x>10:one": If the part's x is more than 10, send the part to the workflow named one.
Rule "m<20:two": Otherwise, if the part's m is less than 20, send the part to the workflow named two.
Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is immediately rejected (R).
Rule "A": Otherwise, because no other rules matched the part, the part is immediately accepted (A).
If a part is sent to another workflow, it immediately switches to the start of that workflow instead and never returns.
If a part is accepted (sent to A) or rejected (sent to R), the part immediately stops any further processing.

The system works, but it's not keeping up with the torrent of weird metal shapes.
The Elves ask if you can help sort a few parts and give you the list of workflows and some part ratings (your puzzle input).
For example:

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}

The workflows are listed first, followed by a blank line, then the ratings of the parts the Elves would like you to sort.
All parts begin in the workflow named in.
In this example, the five listed parts go through the following workflows:

{x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
{x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
{x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
{x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
{x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

Ultimately, three parts are accepted.

Adding up the x, m, a, and s rating for each of the accepted parts gives 7540 for the part with x=787, 4623 for the part with x=2036, and 6951 for the part with x=2127.

Adding all of the ratings for all of the accepted parts gives the sum total of 19114.

Sort through all of the parts you've been given; what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?

--- Part Two ---

Even with your help, the sorting process still isn't fast enough.

One of the Elves comes up with a new plan: rather than sort parts individually through all of these workflows, maybe you can figure out in advance which combinations of ratings will be accepted or rejected.

Each of the four ratings (x, m, a, s) can have an integer value ranging from a minimum of 1 to a maximum of 4000.
Of all possible distinct combinations of ratings, your job is to figure out which ones will be accepted.

In the above example, there are 167409079868000 distinct combinations of ratings that will be accepted.

Consider only your list of workflows; the list of part ratings that the Elves wanted you to sort is no longer relevant.

How many distinct combinations of ratings will be accepted by the Elves' workflows?

"""

"""
for xmas
part defined as a range: min, max (inclusive)
starting part is: 1, 4000: x, m, a, s

apply rule : 
in{s<1351:px,qqz} for each part
apply the test and divide the part into 2 parts, the passing part which goes to true, the failing part which goes to false

px{a<2006:qkq,m>2090:A,rfg}

"""

X = 0
M = 1
A = 2
S = 3
RULE = 4

TEST_LESS = 0
TEST_GREATER = 1
TEST_TRUE = 2

parts = []
ruleIndexes = {}
rules = []

def parse(lines):
    global parts, rules
    parts.clear()
    ruleIndexes.clear()
    rules.clear()
    foundRules = False
    foundParts = False
    for l in lines:
        l = l.strip()
        if not len(l):
            if not foundRules:
                foundRules = True
                continue
            foundParts = True
            continue
        if not foundParts:
            foundRules = True
            # Parse rule
            # rfg{s<537:gd,x>2440:R,A}
            # <name>{<condition>:<destination>,<condition>:<destination>}
            name = l[0:l.index('{')]
            l = l[l.index('{')+1:l.index('}')]
            toks = l.split(',')
            rule = []
            for c in toks:
                c = c.strip().split(':')
                part = None
                test = TEST_TRUE
                value = 0
                dest = None
                if '<' in c[0] or '>' in c[0]:
                    if c[0][0] == 'x':
                            part = X
                    elif c[0][0] == 'm':
                        part = M
                    elif c[0][0] == 'a':
                        part = A
                    elif c[0][0] == 's':
                        part = S
                    if c[0][1] == '<':
                        test = TEST_LESS
                    else:
                        test = TEST_GREATER
                    value = int(c[0][2:])
                    dest = c[1]
                else:
                    dest = c[0]
                    part = RULE
                rule.append((part, test, value, dest))
            ruleIndexes[name] = len(rules)
            rules.append(rule)
        else:
            # Parse part
            # {x=787,m=2655,a=1222,s=2876}
            toks = l[1:-1].split(',')
            part = [0, 0, 0, 0, 0, 0, 0, 0]
            for t in toks:
                c = t.split('=')
                value = int(c[1])
                if c[0] == 'x':
                        part[2*X+0] = value
                        part[2*X+1] = value
                elif c[0] == 'm':
                        part[2*M+0] = value
                        part[2*M+1] = value
                elif c[0] == 'a':
                        part[2*A+0] = value
                        part[2*A+1] = value
                elif c[0] == 's':
                        part[2*S+0] = value
                        part[2*S+1] = value
            parts.append(part)

def runRule1(part, rule):
    for cond in rule:
        var, test, value, dest = cond
        if var == RULE:
            return dest
        min_amount = part[var*2+0]
        max_amount = part[var*2+1]
        if test == TEST_LESS:
           if max_amount < value:
                return dest
        elif test == TEST_GREATER:
           if min_amount > value:
                return dest
    return None

def solvePart1(lines):
    global rules, parts
    parse(lines)
    result = 0
    startRule = ruleIndexes['in']
    for p in parts:
        rule = rules[startRule]
        while True:
            dest = runRule1(p, rule)
            if dest == 'A':
                result += sum(p[v] for v in range(0, 8, 2))
                break
            if dest == 'R':
                break
            rule = rules[ruleIndexes[dest]]
            if dest == 'in':
                return -1

    return result

def solvePart2(lines):
    global rules
    parse(lines)
    result = 0
    startRule = ruleIndexes['in']
    p = [1, 4000, 1, 4000, 1, 4000, 1, 4000]
    parts.clear()
    parts.append(p)
    while len(parts) > 0:
        p = parts.pop()
        rule = rules[startRule]
        while True:
            dest = None
            for cond in rule:
                var, test, value, dest = cond
                if var != RULE:
                    min_amount = p[var*2+0]
                    max_amount = p[var*2+1]
                    if test == TEST_LESS:
                        if max_amount < value:
                            break
                        elif min_amount < value:
                            p2 = p.copy()
                            # min -> value-1
                            p[var*2+1] = value-1
                            # value -> max
                            p2[var*2+0] = value
                            parts.append(p2)
                            break
                    elif test == TEST_GREATER:
                        if min_amount > value:
                            break
                        elif max_amount > value:
                            p2 = p.copy()
                            # value+1 -> max
                            p[var*2+0] = value+1
                            # min -> value
                            p2[var*2+1] = value
                            parts.append(p2)
                            break
                                
            if dest == 'A':
                result += math.prod(p[v*2+1]-p[v*2+0]+1 for v in range(0, 4))
                break
            if dest == 'R':
                break
            rule = rules[ruleIndexes[dest]]
            if dest == 'in':
                return -1

    return result

def main():
    aoc.run_day(19, solvePart1, 323625, solvePart2, 456)

if __name__ == '__main__':
    main()