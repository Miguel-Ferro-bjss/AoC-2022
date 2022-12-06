
def points(c: str):

    s = 'abcdefghijklmnopqrstuvwxyz'
    
    if c == c.capitalize():
        return s.index(c.lower()) + 27

    return s.index(c) + 1

def get_repeated(c1, c2):
    for c in c1:
        if c in c2:
            return points(c)

def get_repeated2(r1, r2, r3):
    for c in r1:
        if c in r2 and c in r3:
            return points(c) 

def run():
    
    f = open('input.txt','r').read().rstrip().split()

    r = 0
    for line in f:
        l = len(line)//2
        r += get_repeated(line[0:l], line[l::])
    
    print(r)

    res = 0
    for i in range(0, len(f)-2, 3):
        res += get_repeated2(f[i], f[i+1], f[i+2])

    print(res)

if __name__ == '__main__':
    run()