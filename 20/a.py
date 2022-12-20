f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')


KEY = 811589153




def decrypt(p=1):

  key = KEY if p==2 else 1

  code = []

  for i, line in enumerate(f):
    code.append((i,int(line)*key))

  def visualize():
    vis = ['e']*len(code)
    for c in code:
      vis[c[0]] = c[1]
    print(vis)
    print()

  # visualize()
  r = 10 if p==2 else 1
  for it in range(r):
    print(it+1, '/', r)
    for i,x in enumerate(code):
      if x[1] == 0:
        continue

      new_pos = (x[0] + x[1])%(len(code)-1)
      if x[1] < 0:
        if new_pos == 0:
          new_pos = len(code) - 1

      #shift other numbers
      if new_pos > x[0]:
        for j,y in enumerate(code):
          if y[0] > x[0] and y[0] <= new_pos:
            code[j] = (y[0]-1, y[1])
      elif new_pos < x[0]:
        for j,y in enumerate(code):
          if y[0] < x[0] and y[0] >= new_pos:
            code[j] = (y[0]+1, y[1])

      code[i] = (new_pos, x[1])

      # print(x[1], ' to ', new_pos)
      # visualize()

  i = 0
  for c in code:
    if c[1] == 0:
      i = c[0]

  vals = (1000, 2000, 3000)
  vals = tuple([(v+i)%len(code) for v in vals])

  #debugging
  # for c in code:
  #   if c[0] > len(code) - 1 or c[0] < 0:
  #     print('problem: ', c[0], c[1])


  # visualize()

  s = 0
  for c in code:
    if c[0] in vals:
      # print(c[1])
      s += c[1]

  print(s)

decrypt(p=1)
decrypt(p=2)
