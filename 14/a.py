def run():

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    rock_to_draw = []
    for line in f:
        points = []
        coord = line.split(" -> ")
        for c in coord:
            cx, cy = c.split(',')
            points.append((int(cx), int(cy)))
        # print(points)
        for i in range(len(points)-1):
            # print(points[i], points[i+1])
            rtd = trace_rock(points[i], points[i+1])
            for rock in rtd:
                rock_to_draw.append(rock)
    
    xx = [x[0] for x in rock_to_draw]
    yy = [x[1] for x in rock_to_draw]

    r = max(xx) - min(xx) + 2
    c = max(yy) + 1

    grid = []
    for i in range(c):
        grid.append(['.' for _ in range(r)])
        # print(' '.join(grid[i]))

    x_shift = min(xx) - 1
    for rock in rock_to_draw:
        x = rock[0] - x_shift
        y = rock[1]
        grid[y][x] = '#'

    # draw sand fountain
    grid[0][500-x_shift] = '+'

    sf = 1
    count = 0
    while (sf):
        sf = sand_fall(grid, x_shift)
        if sf:
            grid[sf[1]][sf[0]] = 'o'
            count += 1
    
    print(count)

    #use a big number and pray
    for _ in range(1000):
        for i in range(len(grid)):
            grid[i].insert(0, '.')
            grid[i].append('.')

    grid.append(['.' for _ in range(len(grid[0]))])
    grid.append(['#' for _ in range(len(grid[0]))])

    sf_ind = grid[0].index('+')
    x_shift = 500 - sf_ind
    
    sf = 1
    while (sf != (500-x_shift, 0)):
        sf = sand_fall(grid, x_shift, part2 = True)
        grid[sf[1]][sf[0]] = 'o'
        count += 1
        # print(count)
    print(count)

    # for g in grid:
    #     print(' '.join(g))

def sand_fall(grid, xx, part2 = False):
    falling = True
    x = 500 - xx
    y = 0
    while(falling and y < len(grid) - 1 and x < len(grid[0]) - 1 and x > 0):
        if grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x += -1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            falling = False
            break
    
    if part2 and (y == len(grid) - 2 or x == 0 or x == len(grid[0]) - 1):
            falling = False
    if not falling:
        return (x, y)
    return False



def trace_rock(p1, p2):
    rock_path = []
    if p1[0] == p2[0]:
        if p2[1] > p1[1]:
            s = p1
            f = p2
        else:
            s = p2
            f = p1
    if p1[1] == p2[1]:
        if p2[0] > p1[0]:
            s = p1
            f = p2
        else:
            s = p2
            f = p1
    for i in range(s[0], f[0]+1):
        for j in range(s[1], f[1]+1):
            # print(i, j)
            rock_path.append((i, j))

    # print('rp', rock_path)
    return rock_path

if __name__ == '__main__':
    run()