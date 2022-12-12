def run():

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')

    elevation = 'abcdefghijklmnopqrstuvwxyzE'

    start_pos = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == 'a' or f[i][j] == 'S':
                start_pos.append((i,j))
    
    paths = [[x] for x in start_pos]
    i = 0
    visited = [x for x in start_pos]
    flag = True
    while(flag): 
        for p in paths:
            # print('path', p)
            new_pos = moves(f, p[-1], elevation, visited)
            if (len(new_pos) == 0):
                paths = [x for x in paths if x != p]
                continue
            # print('new pos', new_pos)
            for np in new_pos:
                visited.append(np)
                pc = p.copy()
                pc.append(np)
                paths.append(pc)
                if f[np[0]][np[1]] == 'E':
                    flag = False
                    break

            paths = [x for x in paths if x != p]
            # print('paths', paths)
            
            if not flag:
                paths = [pc]
                break
            

    steps = 0
    for p in paths:
        if f[p[-1][0]][p[-1][1]] == 'E':
            steps = len(p)
            break
    
    for s in paths[0]:
        print(s, f[s[0]][s[1]])
    print(steps-1)

        # append moves to graph of possible paths
        # don't allow moves that go to already visited pos
 
    

def moves(grid, pos, elevation, visited):
    moves = []
    if pos[0] > 0:
        moves.append((-1, 0))
    if pos[0] < len(grid) - 1:
        moves.append((1, 0))
    if pos[1] > 0:
        moves.append((0, -1))
    if pos[1] < len(grid[0]) - 1:
        moves.append((0, 1))

    # print(moves)
    


    lm = []
    for x in moves:
        current = grid[pos[0]][pos[1]]
        future = grid[pos[0]+x[0]][pos[1]+x[1]]
        future_pos = (pos[0]+x[0], pos[1]+x[1])
        if current == 'S':
            lm = [(pos[0]+m[0], pos[1]+m[1]) for m in moves]
            break
        if current in 'yz' and future == 'E':
            return [future_pos]
        if future == 'S':
            continue
        if (elevation.index(future) - elevation.index(current) <= 1):
            if future_pos not in visited:
                lm.append(future_pos)
    
    return lm

if __name__ == '__main__':
    run()