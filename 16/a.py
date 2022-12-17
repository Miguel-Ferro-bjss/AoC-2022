from collections import deque
from itertools import chain, combinations

"""
A lot of this was 'stolen' from hyper-neutrino's walkthrough on Youtube.
I didn't have the courage to implement the caching mechanism with the bitmask,
so I just waited and used my raging CPU fan as a space heater :)
"""

def parse_input():

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    data = {}

    for line in f:
        valve_part, tunnels_part = line.split(';')
        valve = valve_part.split(" ")[1]
        flow = int(valve_part.split("=")[1])
        tunnels = tunnels_part.split("valve")[1]
        if tunnels[0] == 's':
            tunnels = tunnels[2::].split(", ")
        else:
            tunnels = [tunnels[1::]]
        
        data[valve] = {}
        data[valve]['flow'] = flow
        data[valve]['tunnels'] = tunnels
    
    return data

data = parse_input()

flow_valves = []
for k, v in data.items():
    if v['flow'] > 0:
        flow_valves.append(k)

# get time distance from each 0-flow valve to each flow_valve
time_to = {}
for valve in data:
    if valve in flow_valves or valve == 'AA':
        time_to[valve] = {} # this will store the time distance of a valve to the flow_valves
        checked = {valve} # no point in going where we already are

        queue = deque([(0, valve)])
        
        while queue:
            t_elapsed, current = queue.popleft()
            for adjacent in data[current]['tunnels']:
                if adjacent in checked: # dont check the same thing twice
                    continue
                checked.add(adjacent)
                if data[adjacent]['flow']: # only care about flow_valves
                    time_to[valve][adjacent] = t_elapsed + 1
                queue.append((t_elapsed + 1, adjacent))

# print(time_to)

def optimum_steps(time, valve, opened):

    max_release = 0
    for adjacent in time_to[valve]:
        if adjacent in opened:
            continue # no point in oppening an open valve
        time_remaining = time - time_to[valve][adjacent] - 1 # we open the valve
        if time_remaining < 1: # no time to get any flow
            continue # nothing possible to do
        op = opened.copy()
        op.append(adjacent)
        max_release = max(max_release, optimum_steps(time_remaining, adjacent, op) + data[adjacent]['flow'] * time_remaining)
  
    return max_release

print(optimum_steps(30, 'AA', []))

# number of ways in which we can split the existing valves between 2 workers

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

partitions = powerset(flow_valves)
partitions = [x for x in partitions if len(x) != 0 and len(x) != len(flow_valves)]

max_release = 0
for p in partitions:
    my_valves = list(p)
    el_valves = [x for x in flow_valves if x not in my_valves]
    # print(my_valves, el_valves)
    max_release = max(max_release, optimum_steps(26, 'AA', my_valves) + optimum_steps(26, 'AA', el_valves))

print(max_release)