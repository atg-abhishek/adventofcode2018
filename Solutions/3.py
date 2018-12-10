import re
data = []
with open("../Data/Day3.txt") as infile:
    data = infile.readlines()

def refine_data():
    refined_data = {}
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
        refined_data[int(id_number)] = {
                    
                    "left": int(left_distance),
                    "top": int(top_distance),
                    "rows": int(rows),
                    "columns": int(columns),
                    "coords": []
                }
            
        
    return refined_data

def add_squares(id_number, left, top, num_rows, num_cols, s):
    
    for i in range(left, left+num_cols):
        for j in range(top, top+num_rows):
            coord = str(i)+","+str(j)
            if coord in s.keys():
                s[coord]['count'] += 1
                s[coord]['id'].add(id_number)
            else:
                s[coord] = {}
                s[coord]['count'] = 1
                s[coord]['id'] = set()
                s[coord]['id'].add(id_number)
    return s


def part1():
    s = {}
    total = 0
    refined_data = refine_data()
    for k, item in refined_data.items():
        s = add_squares(k ,item['left'], item['top'], item['rows'], item['columns'], s)
    for k,v in s.items():
        if v['count'] >= 2:
            total += 1
    return (refined_data, total, s)

def part2():
    refined_data, total, s = part1()
    
    for k, v in s.items():
        for id_element in v['id']:
            refined_data[id_element]['coords'].append(k)

    for rectangle_id, data in refined_data.items():
        coords = data['coords']
        overlap = False
        for c in coords:
            if s[c]['count'] > 1:
                overlap = True
                break
        if not overlap:
            # print(refined_data[])
            return rectangle_id
            



print(part2())