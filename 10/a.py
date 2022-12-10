def run():

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')
    # print(f)
    important_cycles = [20 + x for x in range(0, 221, 40)]
    # print(important_cycles)
    cycles = [1]
    V = 0
    for line in f:
        if V != 0:
            cycles.append(cycles[-1])
            cycles.append(cycles[-1]+V)
        if line == "noop":
            cycles.append(cycles[-1])
            V = 0
        else:
            V = int(line.split(" ")[-1])

    streght = 0
    for i in important_cycles:
        print(cycles[i-1])
        streght += i*cycles[i-1]
    
    print()
    print(streght)

    crt = []
    i = 0
    row = []
    for x in cycles:
        if i < 40:
            sprite_pos = [x-ii for ii in range(-1,2,1)]
            if i in sprite_pos:
                row.append('#')
            else:
                row.append(' ') # should be . but it's easier to visualize like this
        else:
            crt.append(''.join(row))
            row = []
            i = 0

        i += 1

    print()
    print('\n'.join(crt))

if __name__ == '__main__':
    run()