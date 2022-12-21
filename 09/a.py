import numpy as np

def run():
    #code to run
    # f = open('input.txt', 'r').read().strip().split('\n')
    f = open('input.txt', 'r').read().strip().split('\n')
    
    rope_1 = np.zeros(shape=(2,2), dtype='int')
    rope_2 = np.zeros(shape=(10,2), dtype='int')
    pos_1 = [rope_1[0].tolist()]
    pos_2 = [rope_2[0].tolist()]
    for line in f:
        
        instruction = line.split()
        direction = instruction[0]
        steps = int(instruction[1])

        for i in range(steps):
            h_1 = rope_1[0]
            h_2 = rope_2[0]
            if direction == 'R':
                mh = np.array([0,1])
            if direction == 'L':
                mh = np.array([0,-1])
            if direction == 'U':
                mh = np.array([1,0])
            if direction == 'D':
                mh = np.array([-1,0])
            
            h_1 += mh
            h_2 += mh

            rope_1[0] = h_1
            rope_2[0] = h_2

            for i in range(len(rope_1)-1):
                m = move(rope_1[i+1],rope_1[i])
                rope_1[i+1] += m

            for i in range(len(rope_2)-1):
                m = move(rope_2[i+1],rope_2[i])
                rope_2[i+1] += m
            
            t_1 = rope_1[-1]
            t_2 = rope_2[-1]
            if t_1.tolist() not in pos_1:
                pos_1.append(t_1.tolist())
                
            if t_2.tolist() not in pos_2:
                pos_2.append(t_2.tolist())

    print(len(pos_1))
    print(len(pos_2))

def move(t,h):
    if np.abs((h-t)[0]) <= 1 and np.abs((h-t)[1]) <= 1:
        return np.array([0,0])
    
    if (np.abs((h-t)[0]) == 2 and (h-t)[1] == 0) or (np.abs((h-t)[1]) == 2 and (h-t)[0] == 0):
        return (h-t)//2

    if np.abs((h-t)[0]) == 2 and np.abs((h-t)[1]) == 1:
        return np.array([(h-t)[0]//2, (h-t)[1]])
    if np.abs((h-t)[1]) == 2 and np.abs((h-t)[0]) == 1:
        return np.array([(h-t)[0], (h-t)[1]//2])

    #added on part2
    if np.abs((h-t)[1]) == 2 and np.abs((h-t)[0]) == 2:
        return (h-t)//2
    
    return 'wtf' #debuggig

    
if __name__ == '__main__':
    run()