from collections import Counter
lines = []
with open("../Data/Day2.txt") as f:
    lines = f.readlines()

def check_letters(string):
    counts = Counter(string)
    two = False
    three = False
    for k, v in counts.items():
        if v == 2:
            two = True
        if v == 3:
            three = True
    return [two, three]

def part1():
    twos = 0
    threes = 0
    for line in lines:
        two, three = check_letters(line.rstrip())
        if two:
            twos += 1
        if three:
            threes += 1
    return twos*threes

print(part1())
