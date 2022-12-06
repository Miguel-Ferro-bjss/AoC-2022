import re

def allDigits(line: str):
    return re.findall('[0-9]+', line)

def wordAtPos(line: str, separator: str,  pos: int):
    m = re.match(('(\w+)'+separator+('(\w+)'+separator)*(pos-1))[:-1], line)
    return m[pos]

def firstWord(line: str):
    return re.match('([a-z]|[A-Z])+', line)

def secondWord(line: str, separator: str):
    return re.match('(\w+)'+separator+'(\w+)', line)[2]