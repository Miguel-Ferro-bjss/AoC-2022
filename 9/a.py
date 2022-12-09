import numpy as np

def run():
    #code to run
    # f = open('input.txt', 'r').read().strip().split('\n')
    f = open('input.txt', 'r').read().strip().split('\n')
    
    rope = [np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0])]
    # print(rope)
    # print(len(rope))
    pos = [rope[0].tolist()]
    for line in f:
        
        instruction = line.split()
        direction = instruction[0]
        steps = int(instruction[1])

        for i in range(steps):
            h = rope[0]
            if direction == 'R':
                h += np.array([0,1])
            if direction == 'L':
                h += np.array([0,-1])
            if direction == 'U':
                h += np.array([1,0])
            if direction == 'D':
                h += np.array([-1,0])
            
            rope[0] = h
            # print(rope)
            # print(direction)
            for i in range(len(rope)-1):
                m = move(rope[i+1],rope[i])
                # print(m)
                rope[i+1] += m
            # print(rope)
            # print()
            t = rope[-1]
            if t.tolist() not in pos:
                pos.append(t.tolist())
                #print(pos)
                #print()

            # print()
    print(len(pos))

def move(t,h):
    if np.abs((h-t)[0]) <= 1 and np.abs((h-t)[1]) <= 1:
        #print(1)
        return np.array([0,0])
    
    if (np.abs((h-t)[0]) == 2 and (h-t)[1] == 0) or (np.abs((h-t)[1]) == 2 and (h-t)[0] == 0):
        #print(2)
        return (h-t)//2

    if np.abs((h-t)[0]) == 2 and np.abs((h-t)[1]) == 1:
        #print(3)
        return np.array([(h-t)[0]//2, (h-t)[1]])
    if np.abs((h-t)[1]) == 2 and np.abs((h-t)[0]) == 1:
        #print(4)
        return np.array([(h-t)[0], (h-t)[1]//2])

    if np.abs((h-t)[1]) == 2 and np.abs((h-t)[0]) == 2:
        return (h-t)//2
    
    return 'wtf'

    
if __name__ == '__main__':
    run()