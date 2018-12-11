from copy import copy
from operator import itemgetter
data = ""
with open("../Data/Day5.txt") as infile:
    data = infile.read()

def eliminate_characters(inp):
    char_list = list(inp)
    found = False
    for i in range(len(char_list)-1):
        if char_list[i].swapcase() == char_list[i+1]:
            found = True
            break
        else:
            continue
    if found:
        return inp[:i] + inp[i+2:]
    else:
        return None

def part1(chars):
    # inp = "dabAcCaCBAcCcaDA"
    inp = chars
    last = inp
    while inp:
        last = inp
        inp = eliminate_characters(last)
        
    
    return len(last)

def part2(chars):
    inp = chars 
    duplicate_inp = copy(inp)
    duplicate_inp = duplicate_inp.upper()
    letter_set = set(duplicate_inp)
    # print(letter_set)
    results = {}
    for letter in letter_set:
        print("Letter is ", letter)
        lower_letter = letter.lower()
        upper_letter = letter
        new_inp = inp.replace(lower_letter, "")
        new_inp = new_inp.replace(upper_letter, "")
        results[letter] = part1(new_inp)
        print("Results are ", results)
    
    print(min(results.items(), key=itemgetter(1)))

part2(data)
