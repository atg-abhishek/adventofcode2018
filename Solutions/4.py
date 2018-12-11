from datetime import datetime
from datetime import timedelta
from operator import itemgetter
import heapq
data = []
with open('../Data/Day4.txt') as infile:
    data = infile.readlines()

def refine_data():
    refined_data = []
    for line in data:
        # ts = line[line.find("[")+1:line.find("]")]
        tokens = line.split()
        
        date = tokens[0][1:]
        time = tokens[1][:-1]
        dt = datetime.strptime(date+" "+ time, '%Y-%m-%d %H:%M')
        kw = tokens[2]
        guard_id = 0
        command_type = 0 # 0=sleep, 1=wake, 2=guard change
        status = 0 # 0 means sleep, 1 means awake
        if kw == 'wakes':
            status = 1
            command_type = 1
        if kw == 'falls':
            status = 0
            command_type = 0
        if kw == 'Guard':
            command_type = 2
            guard_id = tokens[-3][1:]
        
        refined_data.append(
            {
                "dt": dt,
                "command_type" : command_type,
                "status": None if command_type>1 else status,
                "guard_id": None if command_type <=1 else guard_id
                
            }
        )
    refined_data = sorted(refined_data, key=itemgetter('dt'))
    return refined_data

# refine_data()


def part1():
    
    refined_data = refine_data()
    time_slept = {}
    guard_id = 0
    for line in refined_data:
        if line['command_type'] == 2:
            guard_id = line['guard_id']
        if guard_id in time_slept:
            time_slept[guard_id].append({'status': line['status'], 'dt': line['dt']})
        else:
            time_slept[guard_id] = [{'status': line['status'], 'dt': line['dt']}]
    
    minutes_slept = {}
    tally_sleep = {}
    for k,v in time_slept.items():
        tally_sleep[k] = {x:0 for x in range(60)}
        sleep_start = 0
        sleeping_minutes = timedelta(0)
        for time in v:
            if time['status'] is None:
                continue
            elif time['status'] == 0:
                sleep_start = time['dt']
            elif time['status'] == 1:
                sleeping_minutes += (time['dt'] - sleep_start)
                for i in range(sleep_start.minute, time['dt'].minute):
                    tally_sleep[k][i] += 1
                
        minutes_slept[k] = sleeping_minutes.total_seconds()
    
    max_sleeping_guard = max(minutes_slept.items(), key=itemgetter(1))
    max_minute_slept = max(tally_sleep[max_sleeping_guard[0]].items(), key=itemgetter(1))
    
    print(int(max_sleeping_guard[0])*max_minute_slept[0])

    return tally_sleep

# part1()

def part2():
    '''
    for each minute, write down minutes slept and indicate guard 

    '''
    tally_sleep = part1()
    by_minutes = {x:{} for x in range(60)}
    for k, v in tally_sleep.items():
        for i,j in v.items():
            by_minutes[i][k] = j
    
    minute_ratios = {}
    for k,v in by_minutes.items():
        # print("k ", k)
        largest_two = heapq.nlargest(2, v.items(), key=itemgetter(1))
        minute_ratios[k] = largest_two[0][1] - largest_two[1][1]
        # print('\n')
    
    minute_result = max(minute_ratios.items(), key=itemgetter(1))
    print(minute_result)
    guard_result = max(by_minutes[minute_result[0]].items(), key=itemgetter(1))[0]
    print(guard_result)
    print(int(guard_result)*minute_result[0])

part2()
