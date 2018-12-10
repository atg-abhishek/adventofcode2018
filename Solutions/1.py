lines = []
with open('../Data/Day1.txt') as f:
    lines = f.readlines()
total = 0
for line in lines:
    str_frequency = line.rstrip()
    sign = str_frequency[0]
    num = 0 
    if sign == "-":
        num = 0-int(str_frequency[1:])
    else:
        num = int(str_frequency[1:])
    total+=num
print(total)