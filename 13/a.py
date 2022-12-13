from functools import cmp_to_key

def run():

    f = open('input.txt', 'r').read().strip().split('\n\n')
    # f = open('test.txt', 'r').read().strip().split('\n\n')

    count_right_order = 0
    ordered = []

    for i in range(len(f)):
        pair = f[i].split('\n')
        # print('\n'j+ str(i + 1))
        # print(pair)
        p1 = eval(pair[0])
        p2 = eval(pair[1])
        c = compare(p1, p2)
        # print(c)
        if c == -1:
            count_right_order += i+1
        
        ordered.append(p1)
        ordered.append(p2)

    dividers = [[[2]], [[6]]]
    for d in dividers:
        ordered.append(d)

    ordered = sorted(ordered, key=cmp_to_key(lambda l1, l2: compare(l1, l2)))

    key = 1
    for d in dividers:
        key *= ordered.index(d) + 1 

    print(count_right_order)
    print(key)

def compare(l1, l2):
    # print(l1, l2)
    if type(l1) == int and type(l2) == int:
        if l1 > l2:
            return 1
        elif l1 < l2:
            return -1
        return 0

    elif type(l1) == list and type(l2) == list:
        i = 0
        while i < len(l1) and i < len(l2):
            c = compare(l1[i], l2[i])
            if c == 1 or c == -1:
                return c
            i += 1
        if i == len(l1) and i<len(l2):
            return -1
        elif i == len(l2) and i < len(l1):
            return 1
        else:
            return 0
    
    elif type(l1) == list and type(l2) == int:
        return compare(l1, [l2])
    else:
        return compare([l1], l2)

if __name__ == '__main__':
    run()