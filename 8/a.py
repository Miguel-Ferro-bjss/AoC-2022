import numpy as np

def run():
    #code to run
    f = open('input.txt','r').readlines()
    grid = np.zeros(shape=(len(f), len(f[0][:-1])), dtype='int')

    for i in range(len(f)):
        if i == len(f) - 1:
            line = f[i]
        else:
            line = f[i][:-1]
        grid[i] = [int(x) for x in line]

    def leftScene(i,j):
        c = 0
        for t in np.flipud(grid[i,0:j]):
            if t < grid[i,j]:
                c += 1
            else:
                return c + 1
        return c

    def rightScene(i,j):
        c = 0
        for t in grid[i,j+1::]:
            if t < grid[i,j]:
                c += 1
            else:
                return c + 1
        return c

    def topScene(i,j):
        c = 0
        for t in np.flipud(grid[0:i,j]):
            if t < grid[i,j]:
                c += 1
            else:
                return c + 1
        return c

    def bottomScene(i,j):
        c = 0
        for t in grid[i+1::,j]:
            if t < grid[i,j]:
                c += 1
            else:
                return c + 1
        return c

    count = 0
    scene = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            x = grid[i,j]
            if (grid[i,0:j] < x).all() or (grid[i,j+1::] < x).all() or (grid[0:i,j] < x).all() or (grid[i+1::,j] < x).all():
                count += 1
        
            scene = max(scene, leftScene(i,j)*rightScene(i,j)*topScene(i,j)*bottomScene(i,j))


            

    count += len(grid)*2 + len(grid[0])*2 - 4

    print(count)
    print(scene)
if __name__ == '__main__':
    run()