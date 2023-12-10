import aoc

"""
--- Day 7: Camel Cards ---
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship.
(At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time.
You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon.
The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there.
Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help.
You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards.
Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type.
From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect.
Start by comparing the first card in each hand.
If these cards are different, the hand with the stronger first card is considered stronger.
If the first card in each hand have the same label, however, then move on to considering the second card in each hand.
If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger.
Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input).
For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

This example shows five hands; each hand is followed by its bid amount.
Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand.
Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair.
Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind.
QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5).
So the total winnings in this example are 6440.

Find the rank of every hand in your set.
What are the total winnings?

Your puzzle answer was 246912307.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule.
Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2.
The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind.
However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set.
What are the new total winnings?
"""

values = {}

def prepare1():
    # A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
    v = 13
    for c in "AKQJT98765432":
        values[c] = v
        v -= 1

def prepare2():
    # The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.
    v = 13
    for c in "AKQT98765432J":
        values[c] = v
        v -= 1

# Rank the hands
# 6 = Five of a kind, where all five cards have the same label: AAAAA
# 5 = Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 4 = Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 3 = Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 2 = Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 1 = One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 0 = High card, where all cards' labels are distinct: 23456
# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
def rank_hand(hand):
    counts = {}
    for c in "AKQJT98765432":
        counts[c] = 0
    for c in hand:
        counts[c] += 1
    threes = 0
    pairs = 0
    for c in counts.values():
        if c == 5:
            return 6
        elif c == 4:
            return 5
        elif c == 3:
            threes += 1
        elif c == 2:
            pairs += 1
    if threes == 1 and pairs == 1:
        return 4
    if threes == 1 and pairs == 0:
        return 3
    if threes == 0 and pairs == 2:
        return 2
    if threes == 0 and pairs == 1:
        return 1
    if threes == 0 and pairs == 0:
        return 0
    
    exit("bad rank hand:" + hand)

# J cards can pretend to be whatever card is best for the purpose of determining hand type; 
# for example, QJJQ2 is now considered four of a kind.

def rank_hand2(hand):
    counts = {}
    for c in "AKQJT98765432":
        counts[c] = 0
    for c in hand:
        counts[c] += 1
    threes = 0
    pairs = 0
    jokers = counts['J']
    for k in counts:
        v = counts[k]
        if v == 0:
            continue
        if v == 5:
            return 6
        if k == 'J':
            continue
        if v+jokers == 5:
            return 6
        elif v+jokers == 4:
            return 5
        elif v == 3:
            threes += 1
        elif v == 2:
            pairs += 1
    if jokers == 2 and pairs == 0:
        threes += 1
    elif jokers == 1 and pairs > 0:
        threes += 1
        pairs -= 1
    elif jokers == 1 and pairs == 0:
        pairs += 1
    
    if threes == 1 and pairs == 1:
        return 4
    if threes == 1 and pairs == 0:
        return 3
    if threes == 0 and pairs == 2:
        return 2
    if threes == 0 and pairs == 1:
        return 1
    if threes == 0 and pairs == 0:
        return 0
    
    exit("bad rank hand:" + hand)

def hand_greater(rank_i, rank_j, hand_i, hand_j):
    if rank_j > rank_i:
        return False
    # Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.
    if rank_i > rank_j:
        return True

    # If two hands have the same type, a second ordering rule takes effect.
    # A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
    # The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
    # Start by comparing the first card in each hand.
    # If these cards are different, the hand with the stronger first card is considered stronger.
    # If the first card in each hand have the same label, however, then move on to considering the second card in each hand.
    # If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.
    for c in range(5):
        card_i = values[hand_i[c]]
        card_j = values[hand_j[c]]
        if card_i > card_j:
            return True
        if card_i < card_j:
            return False
    return False

def solvePart1(lines):
    prepare1()
    result = 0
    hands = []
    bids = []
    for l in lines:
        if l.strip() == "":
            continue
        toks = l.strip().split()
        hands.append(toks[0])
        bids.append(int(toks[1]))

    ranks = []
    for i in range(len(hands)):
        ranks.append((i,rank_hand(hands[i])))

    for i in range(len(ranks)-1):
        for j in range(i+1, len(ranks)):
            hand_i = hands[ranks[i][0]]
            hand_j = hands[ranks[j][0]]
            rank_i = ranks[i][1]
            rank_j = ranks[j][1]
            if hand_greater(rank_i, rank_j, hand_i, hand_j):
                temp = ranks[j]
                ranks[j] = ranks[i]
                ranks[i] = temp
        
    result = 0
    for i in range(len(ranks)):
        result += (bids[ranks[i][0]] * (i+1))
    return result

def solvePart2(lines):
    prepare2()
    result = 0
    hands = []
    bids = []
    for l in lines:
        if l.strip() == "":
            continue
        toks = l.strip().split()
        hands.append(toks[0])
        bids.append(int(toks[1]))

    ranks = []
    for i in range(len(hands)):
        ranks.append((i,rank_hand2(hands[i])))

    for i in range(len(ranks)-1):
        for j in range(i+1, len(ranks)):
            hand_i = hands[ranks[i][0]]
            hand_j = hands[ranks[j][0]]
            rank_i = ranks[i][1]
            rank_j = ranks[j][1]
            if hand_greater(rank_i, rank_j, hand_i, hand_j):
                temp = ranks[j]
                ranks[j] = ranks[i]
                ranks[i] = temp
        
    result = 0
    for i in range(len(ranks)):
        result += (bids[ranks[i][0]] * (i+1))
    return result

def main():
    aoc.run_day(7, solvePart1, 246912307, solvePart2, 246894760)

if __name__ == '__main__':
    main()