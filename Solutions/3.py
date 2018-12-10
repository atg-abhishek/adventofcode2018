import re
data = []
with open("../Data/Day3.txt") as infile:
    data = infile.readlines()

def refine_data():
    refined_data = []
    for line in data:
        line = line.rstrip()
        tokens = line.split(" ")
        id_number = re.sub("#", "", tokens[0])
        distances = tokens[2].split(",")
        left_distance = distances[0]
        top_distance = distances[1][:-1]
        sizes = tokens[-1].split("x")
        columns = sizes[0]
        rows = sizes[1]
        refined_data.append(
            {
                "id" : int(id_number),
                "left": int(left_distance),
                "top": int(top_distance),
                "rows": int(rows),
                "columns": int(columns)
            }
        )
    return refined_data

def add_squares(left, top, num_rows, num_cols, s):
    
    for i in range(left, left+num_cols):
        for j in range(top, top+num_rows):
            coord = str(i)+","+str(j)
            if coord in s.keys():
                s[coord] += 1
            else:
                s[coord] = 1
    return s


def part1():
    s = {}
    total = 0
    refined_data = refine_data()
    for item in refined_data:
        s = add_squares(item['left'], item['top'], item['rows'], item['columns'], s)
    for k,v in s.items():
        if v >= 2:
            total += 1
    return total

print(part1())