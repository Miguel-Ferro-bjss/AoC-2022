
stream = open('input.txt', 'r').read()
# stream = open('test.txt', 'r').read()

rocks = {'-': [(0,0), (1,0), (2,0), (3,0)], '+': [(0,0), (0,1), (0,2), (-1,1), (1,1)], 'L': [(0,0), (1,0),(2,0), (2,1), (2,2)], '|': [(0,0), (0,1),(0,2),(0,3)], 's': [(0,0), (1,0), (0,1), (1,1)]}
moves = {'<': (-1,0), '>': (1,0), 'v': (0,-1)}
keys = list(rocks.keys())

grid = []
for i in range(4):
    row = []
    for j in range(7):
        row.append('.')
    grid.append(row)

def move_rock(rock, move):
    r = [(move[0] + coord[0], move[1] + coord[1]) for coord in rock]
    return r

def highest_rock(grid):
    for i, row in enumerate(grid[::-1]):
        if '#' in row:
            return len(grid) - i
    return 0


def possible_pos(rock, grid):
    for p in rock:
        if p[0] < 0 or p[0] >= len(grid[0]) or p[1] < 0:
            return False
        elif grid[p[1]][p[0]] == '#':
            return False
    return True

def draw_rock(rock, grid):
    for p in rock:
        grid[p[1]][p[0]] = "#"

    return grid

s_i = 0
for i in range(2022):

    key = keys[i % len(keys)]
    rock = rocks[key]

    highest = highest_rock(grid)
    if key != '+':
        rock = move_rock(rock, (2, highest + 3)) # initialize rock
    else:
        rock = move_rock(rock, (3, highest + 3))
    # print(rock)

    for _ in range(3):
        row = []
        for _ in range(7):
            row.append('.')
        grid.append(row)

    while True:
        m = moves[stream[s_i % len(stream)]] #stream move (x,y)
        s_i += 1
        new_rock = move_rock(rock, m)
        if possible_pos(new_rock, grid):
            rock = new_rock
            # print(rock)
        m = moves['v'] #move down (x,y)
        new_rock = move_rock(rock, m)
        if possible_pos(new_rock, grid):
            rock = new_rock
            # print(rock)
        else:
            # print(rock)
            grid = draw_rock(rock, grid)
            break
    
    # for g in grid[::-1]:
    #     print(' '.join(g))
    # print('\n')

print(highest_rock(grid))