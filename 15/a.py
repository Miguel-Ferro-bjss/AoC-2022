import re

def parse_input():
    part1 = True
    part2 = True
    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')
    sensors = []
    beacons = []
    for line in f:
        sx, sy, bx, by = [int(x) for x in re.findall('-?[0-9]+', line)]
        sensors.append((sx, sy))
        beacons.append((bx, by))
    
    return sensors, beacons

def part1(sensors, beacons):
    forbidden_pos = set()
    target = 2000000
    # target = 10
    for s,b in zip(sensors, beacons):
        d = dist(s, b)
        c = (s[0]-d, s[0]+d)
        for i in range(c[0], c[1]):
            if d >= dist(s, (i,target)) and (i,target) not in beacons:
                forbidden_pos.add((i,target))


    count = len([x for x in forbidden_pos if x[1]==target])
    print(count)

def part2(sensors, beacons):

    limit = 4000000
    found = False
    for s,b in zip(sensors, beacons):
        edges = sensor_edges(s, b)
        for e in edges:
            if valid(e, sensors, beacons, limit):
                print(e[0]*limit + e[1])
                found = True
                assert not found


def valid(p, sensors, beacons, limit):
    if p[0] > limit or p[0] < 0 or p[1] > limit or p[1] < 0:
        return False
    for s,b  in zip(sensors, beacons):
        if dist(s, p) <= dist(s, b):
            return False
    return True 


def dist(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def sensor_edges(s, b):

    d = dist(s, b)
    edge = []
    jj = 0
    for i in range(s[0]-d-1, s[0]+1):
        edge.append((i, s[1]-jj))
        edge.append((i, s[1]+jj))
        jj += 1

    edges = []
    for e in edge:
        edges.append(e)
        edges.append((s[0] + abs(e[0]-s[0]), e[1]))

    return edges


if __name__ == '__main__':
    s, b = parse_input()

    #these take a good amount of time (1-2 min each)
    part1(s, b)
    part2(s, b)