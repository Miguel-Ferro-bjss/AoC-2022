

def run():

    g = open('input.txt', 'r').readlines()

    f = open('input_a.txt', 'r')
    lines = f.readlines()
    columns = []
    for l in lines:
        c = []
        for i in range(1, len(l), 4):
            c.append(l[i])
        columns.append(c)

    cc = columns
    columns = []

    for i in range(len(cc[0])):
        c = []
        for l in cc:
            if l[i] != ' ':
                c.append(l[i])
        columns.append(c)

    
    moves = []
    for l in g:
        m = []
        for x in l:
            if x in '0123456789':
                m.append(int(x))
        if len(m) > 3:
            m[1] = int(str(m[0])+str(m[1]))
            m = m[1::]
        moves.append(m)
    # print(moves)

    columns = [x[::-1] for x in columns]

    for m in moves:
        col_from = m[1]-1
        col_to = m[2]-1
        num = m[0]
        for i in range(num):
            x = columns[col_from].pop()
            columns[col_to].append(x)

    print(''.join([x[-1] for x in columns if x!=[]]))

    # part 2

    f = open('input_a.txt', 'r')
    lines = f.readlines()
    columns = []
    for l in lines:
        c = []
        for i in range(1, len(l), 4):
            c.append(l[i])
        columns.append(c)

    cc = columns
    columns = []

    for i in range(len(cc[0])):
        c = []
        for l in cc:
            if l[i] != ' ':
                c.append(l[i])
        columns.append(c)

    columns_2 = [x[::-1] for x in columns]

    for m in moves:
        col_from = m[1]-1
        col_to = m[2]-1
        num = m[0]

        x2 = columns_2[col_from][-num::]
        columns_2[col_from] = columns_2[col_from][0:-num]
        for xx in x2:
            columns_2[col_to].append(xx)

    print(''.join([x[-1] for x in columns_2 if x!=[]]))

if __name__ == '__main__':
    run()