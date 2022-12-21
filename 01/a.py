

def run():
    
    f = open('input.txt', 'r').readlines()

    elves = []
    elve = []
    for line in f:
        if line != '\n':
            elve.append(int(line[0:-1]))
        else:
            elves.append(sum(elve))
            elve = []

    # print(elves)
    elves.sort()
    print(max(elves))
    print(sum(elves[-3::]))

if __name__ == '__main__':
    run()