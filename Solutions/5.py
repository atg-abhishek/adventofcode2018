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

def part1():
    # inp = "dabAcCaCBAcCcaDA"
    inp = data
    last = inp
    while inp:
        last = inp
        inp = eliminate_characters(last)
        
    
    print(len(last))

part1()
