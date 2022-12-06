def allDifferent(m: str):
    return len(m) == len(set(m))

def run1():
    
    f = open('input.txt', 'r').read()
    
    for i in range(len(f)-3):
        marker = f[i:i+4]
        if allDifferent(marker):
            return i+4

def run2():

    f = open('input.txt', 'r').read()
    
    for i in range(len(f)-13):
        start_of_message = f[i:i+14]
        if allDifferent(start_of_message):
            return i+14



if __name__ == '__main__':
    print(run1())
    print(run2())