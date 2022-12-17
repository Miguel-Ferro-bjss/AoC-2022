
stream = open('input.txt', 'r').read()
# stream = open('test.txt', 'r').read()

rocks = {'-': {(0,0), (1,0), (2,0), (3,0)}, '+': {(0,0), (0,1), (0,2), (-1,1), (1,1)}, 'L': {(0,0), (1,0),(2,0), (2,1), (2,2)}, '|': {(0,0), (0,1),(0,2),(0,3)}, 's': {(0,0), (1,0), (0,1), (1,1)}}
moves = {'<': (-1,0), '>': (1,0), 'v': (0,-1)}
keys = list(rocks.keys())

rock_stack = set()

def move_rock(rock, move):
    r = {(x + move[0], y + move[1]) for (x,y) in rock}
    return r

def highest_rock():
    if rock_stack:
        return max(y for (_,y) in rock_stack)
    return -1

def possible_pos(rock):
    for p in rock:
        if p[0] < 0 or p[0] >= 7 or p[1] < 0:
            return False
        elif rock & rock_stack:
            return False
    return True

def stack_rock(rock):
    for p in rock:
        rock_stack.add(p)
    
def draw():
    rows = highest_rock() + 1
    grid = []
    for i in range(0, rows):
        row = []
        for j in range(7):
            d = '#' if (j, i) in rock_stack else '.'
            row.append(d)
        grid.append(row)
    for g in grid[::-1]:
        print(" ".join(g))


def stack_signature():
    # hyper-neutrino to the rescue!
    height_map = [-20] * 7
    for r in rock_stack:
        height_map[r[0]] = max(height_map[r[0]], r[1])
    top = max(height_map)
    return tuple(y - top for y in height_map)

s_i = 0
L = 1000000000000 # part 2
# L = 2022 # part 1
i = 0
seen = {}
while i < L:
    key = keys[i % len(keys)]
    rock = rocks[key]
    h = highest_rock()

    if key != '+':
        rock = move_rock(rock, (2, h + 4)) # initialize rock
    else:
        rock = move_rock(rock, (3, h + 4))

    while True:
        m = moves[stream[s_i % len(stream)]] #stream move (x,y)
        s_i += 1
        new_rock = move_rock(rock, m)
        if possible_pos(new_rock):
            rock = new_rock
            # print(rock)
        m = moves['v'] #move down (x,y)
        new_rock = move_rock(rock, m)
        if possible_pos(new_rock):
            rock = new_rock
            # print(rock)
        else:
            # print(rock)
            stack_rock(rock)
            h = highest_rock()
            seen_key = (s_i % len(stream), key, stack_signature())
            if seen_key in seen:
                # neat trick (credits to hyper-neutrino)
                prev_i, prev_h = seen[seen_key] 
                rocks_remaining = L - i
                rep_remaining = rocks_remaining // (i - prev_i)
                h_offset = rep_remaining * (h - prev_h)
                i += rep_remaining * (i - prev_i)
                seen = {}
                if i >= L:
                    break
            seen[seen_key] = (i, h)
            break
    i += 1
# draw()
print(h + 1 + h_offset)