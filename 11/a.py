from math import floor

def run(part):

    f = open('input.txt', 'r').read().strip().split('\n')
    # f = open('test.txt', 'r').read().strip().split('\n')
    
    monkey = {}
    for line in f:
        words = line.split()
        if len(words) < 1:
            continue
        if words[0] == 'Monkey':
            key = words[1][:-1]
            monkey[key] = {}
        elif words[0] == 'Starting':
            monkey[key]['items'] = [int(x[:-1]) if x[-1] == ',' else int(x) for x in words[2::]]
        elif words[0] == 'Operation:':
            monkey[key]['exp'] = words[3::]
            monkey[key]['operation'] = lambda x, ex: eval(" ".join(ex).replace("old", str(x)))
        elif words[0] == 'Test:':
            monkey[key]['div'] = words[-1]
            monkey[key]['test'] = lambda x, d: x % int(d) == 0
        elif words[0] == 'If':
            monkey[key][words[1][:-1]] = words[-1]
    
    for key in monkey:
        monkey[key]['count'] = 0

    lcm = 1
    for _, v in monkey.items():
        lcm *= int(v['div'])

    rounds = 20
    if part == 2:
        rounds = 10000

    for _ in range(rounds):
        for k, v in monkey.items():
            for item in v['items']:
                #apply operation and rules to item
                item = v['operation'](item, v['exp'])
                if part == 2:
                    item %= lcm
                if part == 1:
                    item = floor(item/3)
                v['count'] += 1
                to = v['true'] if v['test'](item, v['div']) else v['false']
                monkey[to]['items'].append(item)
                v['items'] = v['items'][1::]

        
    counts = sorted([monkey[key]['count'] for key in monkey])[::-1]
    print(counts[0]*counts[1])

if __name__ == '__main__':
    run(1)
    run(2)