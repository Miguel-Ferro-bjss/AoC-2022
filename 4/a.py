def fully_contains(a ,b):
    return (a[0] >= b[0] and a[-1] <= b[-1]) or (b[0] >= a[0] and b[-1] <= a[-1]) 

def overlaps(a, b):
    range_a = range(a[0], a[-1]+1)
    range_b = range(b[0], b[-1]+1)

    for a in range_a:
        if a in range_b:
            return 1
    
    return 0

def run():
    
    f = open('input.txt','r').read().rstrip().split()

    r1 = 0
    r2 = 0
    for line in f:
        s = line.split(',')
        a = s[0].split('-')
        b = s[-1].split('-')
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        r1 += fully_contains(a, b)
        r2 += overlaps(a, b)

    print(r1)
    print(r2)
if __name__ == '__main__':
    run()