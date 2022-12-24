from collections import deque
from numpy import lcm

f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')

walls = set()
blizzards = []
directions = {'>': (1,0), 'v': (0,1), '^': (0,-1), '<': (-1,0), '-': (0,0)}

for y,line in enumerate(f):
  for x,tile in enumerate(line):
    if tile == '#':
      walls.add((x,y))
    elif tile != '.':
      blizzards.append((x,y,tile))

max_x = max([w[0] for w in walls])
max_y = max([w[1] for w in walls])
print('max_x', max_x)
print('max_y', max_y)

def move_blizzards(bl):
  for i,b in enumerate(bl):
    d = directions[b[-1]]
    nb = (b[0]+d[0], b[1]+d[1], b[2])
    if nb[0] >= max_x:
      nb = (1, nb[1], nb[2])
    elif nb[0] <= 0:
      nb = (max_x-1, nb[1], nb[2])
    elif nb[1] >= max_y:
      nb = (nb[0], 1, nb[2])
    elif nb[1] <= 0:
      nb = (nb[0], max_y-1, nb[2])
    
    bl[i] = nb 

  return bl

def in_range(pos):
  if pos[0] >= max_x or pos[0] <= 0:
    return False
  if pos[1] >= max_y or pos[1] <= 0:
    return False
  return True

def blizzard_to_pos(bl):
  return [(b[0], b[1]) for b in bl]

start = (1,0)
finish = (max_x-1, max_y)
print('finish', finish)

bl_key = lcm(max_x-1, max_y-1)

bl = blizzards.copy()
bl_pos = [blizzard_to_pos(bl)]
for i in range(1, bl_key):
  bl = move_blizzards(bl.copy())
  bl_pos.append(blizzard_to_pos(bl))

Q = deque([(start, 0)])
seen = set()
trips = 0
while Q:
  pos, steps = Q.popleft()
  # print('pos', pos, 'steps', steps)
  s = steps + 1
  # check all scenarios (down, left, right, wait, up)
  for d in directions.values():
    np = tuple([pos[i]+d[i] for i in range(2)])
    # print('np', np)
    if ((trips == 0 or trips == 2) and np == finish) or (trips == 1 and np == start):
      print(np, s, trips)
      break
    
    if np not in bl_pos[s%bl_key] and (in_range(np) or np == start or np == finish) and (np, s%bl_key) not in seen:
      Q.append((np, s))
      seen.add((np, s%bl_key))

  if np == finish and trips == 0:
    trips += 1
    Q = deque([(finish, s)])
  elif np == start and trips == 1:
    trips += 1
    Q = deque([(start, s)])
  elif np == finish and trips == 2:
    print(s)
    break