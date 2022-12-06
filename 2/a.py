def calc_match(a: str, b: str):

    bb = convert_points(b)
    
    if a == b:
        return bb + 3
    
    if a == 'A':
        if b == 'B':
            return bb + 6
        return bb
    if a == 'B':
        if b == 'A':
            return bb
        return bb + 6
    if a == 'C':
        if b == 'A':
            return bb + 6
        return bb

    return -1

def read_line(line: str):

    s = line.split(" ")
    a = s[0]
    b = s[1][0]

    b = convert_b(a, b)

    return calc_match(a, b)

def convert_points(b: str):
    if b == 'A':
        return 1
    if b == 'B':
        return 2
    if b == 'C':
        return 3
    print('got -1 on convert points')
    return -1

def convert_b(a: str, b: str):

    if b == 'Y':
        return a
    
    if b == 'X':
        if a == 'A':
            return 'C'
        if a == 'B':
            return 'A'
        return 'B'

    if b == 'Z':
        if a == 'A':
            return 'B'
        if a == 'B':
            return 'C'
        
        return 'A'

def get_total():

    score = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            score += read_line(line)

    return score

if __name__ == '__main__':

    print(get_total())