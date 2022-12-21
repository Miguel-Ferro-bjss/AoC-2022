import copy
import sympy



part = 2

def parse_input(part=1):
  f = open('input.txt', 'r').read().strip().split('\n')
  # f = open('test.txt', 'r').read().strip().split('\n')

  monkey = {}

  for line in f:
    sp = line.split(":")
    name = sp[0]
    data = sp[1].split(" ")
    monkey[name] = {}
    if part == 2:
      if name == 'root':
        monkey[name]['n'] = 'e'
        monkey[name]['op'] = (data[1], data[3], '-') # if root = 0 then they are equal
      elif name == 'humn':
        monkey[name]['n'] = sympy.Symbol("x")
        monkey[name]['op'] = 'e'
      else:
        if len(data) == 2: #its single number
          monkey[name]['n'] = sympy.Integer(data[1])
          monkey[name]['op'] = 'e'
        elif len(data) == 4: #its operation
          monkey[name]['n'] = 'e'
          monkey[name]['op'] = (data[1], data[3], data[2])
    elif part == 1:
      if len(data) == 2: #its single number
        monkey[name]['n'] = int(data[1])
        monkey[name]['op'] = 'e'
      elif len(data) == 4: #its operation
        monkey[name]['n'] = 'e'
        monkey[name]['op'] = (data[1], data[3], data[2]) # (x1, x2, operation)
  
  return monkey

def calc(op):
  
  if op[2] == '+':
    return op[0] + op[1]
  elif op[2] == '-':
    return op[0] - op[1]
  elif op[2] == '*':
    return op[0] * op[1]
  elif op[2] == '/':
    return op[0]/op[1]
  if op[2] == '=':
    return op[0] == op[1]
  

def solve_2(monkey):
  mc = copy.deepcopy(monkey)
  while(True):
    if mc['root']['n'] != 'e':
      print(sympy.solve(mc['root']['n'])[0])
      break
    for name, m in mc.items():
      if m['n'] != 'e':
        continue
      # treat mcs with op and no number
      op = m['op']
      if mc[op[0]]['n'] == 'e' or mc[op[1]]['n'] == 'e':
        continue
      else:
        op_values = (mc[op[0]]['n'], mc[op[1]]['n'], op[2])
        mc[name]['n'] = calc(op_values)
        if name == 'root':
          break
  

def solve_1(monkey):
  mc = copy.deepcopy(monkey)
  while(True):
    if mc['root']['n'] != 'e':
      break
    for name, m in mc.items():
      if m['n'] != 'e':
        continue
      # treat mcs with op and no number
      op = m['op']
      if mc[op[0]]['n'] == 'e' or mc[op[1]]['n'] == 'e':
        continue
      else:
        op_values = (mc[op[0]]['n'], mc[op[1]]['n'], op[2])
        mc[name]['n'] = calc(op_values)
      if mc['root']['n'] != 'e':
        break
  
  print(int(mc['root']['n']))

solve_1(parse_input())
solve_2(parse_input(part=2))
