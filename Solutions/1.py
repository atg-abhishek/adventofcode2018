from itertools import cycle
lines = []
with open('../Data/Day1.txt') as f:
    lines = f.readlines()

def part1():
    total = 0
    for line in lines:
        num=process_input(line)
        total+=num
    print(total)

def process_input(line):
    str_frequency = line.rstrip()
    sign = str_frequency[0]
    num = 0 
    if sign == "-":
        num = 0-int(str_frequency[1:])
    else:
        num = int(str_frequency[1:])
    return num

def part2():
    pool = cycle(lines)
    total = 0
    s = set()
    s.add(total)
    for item in pool:
        num = process_input(item)
        total += num
        if total in s:
            print("Repetition found at ", total)
            break
        else:
            s.add(total)

part2()