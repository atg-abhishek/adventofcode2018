from collections import Counter
from copy import deepcopy
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

def compare_two_strings(s1, s2):
    ok = False
    char_of_diff = ''
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return (c1, False)
            else:
                char_of_diff = c1
                ok = True

    return (char_of_diff, ok)

def part2():
    lines_copy = deepcopy(lines)
    lines_copy.sort()
    chars = set()
    for idx, line in enumerate(lines_copy[:-1]):
        for other_line in lines_copy[idx+1:]:
            res = compare_two_strings(line.rstrip(), other_line.rstrip())
            if res[1]:
                print("this was hit")
                chars = set(line.rstrip()) - set(res[0])
                print(line)
                print(res[0])
                break


    

 


# print(compare_two_strings("abcde", "axcye"))
print(part2())
