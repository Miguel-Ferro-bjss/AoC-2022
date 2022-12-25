def snafu_to_decimal(s):
  res = 0
  for i,digit in enumerate(s):
    if digit == '-':
      digit = -1
    elif digit == '=':
      digit = -2
    else:
      digit = int(digit)
    res += digit*(5**(len(s)-1-i))
  return res

def decimal_to_base5(d):
  res = []
  while True:
    q = d//5
    r = d%5
    res.append(str(r))
    d = q
    if q == 0: break
  
  res = ''.join(res[::-1])
  return res

def decimal_to_snafu(d):
  bf = decimal_to_base5(d)
  s = []
  carry = 0
  for digit in bf[::-1]:
    # print(digit, carry)
    digit = int(digit)
    if carry:
      digit += carry
      carry = 0
    if digit < 3:
      s.append(str(digit))
    elif digit == 3:
      s.append('=')
      carry = 1
    elif digit == 4:
      s.append('-')
      carry = 1
    elif digit == 5:
      s.append('0')
      carry = 1

  if carry:
    s.append('1')
  
  return ''.join(s[::-1])

f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')

fuel = 0
for s in f:
  d = snafu_to_decimal(s)
  fuel += d

print(decimal_to_snafu(fuel))