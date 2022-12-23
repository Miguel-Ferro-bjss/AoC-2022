# part 1 got broken when I adapted the code for part 2
# part 2 takes a million years

f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')

def get_elves():
  elves = []
  for i,line in enumerate(f):
    for j,tile in enumerate(line):
      if tile == '#':
        elves.append((j,i))
  return elves

elves = get_elves()

# 0:N, 1:S, 2:W, 3:E
main_directions = {0: (0,-1), 1: (0,1), 2: (-1,0), 3: (1,0)}
adj_directions = {0: ((-1,-1), (0,-1), (1,-1)), 1: ((-1,1), (0,1), (1,1)), 2: ((-1,1), (-1,0), (-1,-1)), 3: ((1,1), (1,0), (1,-1))}
all_directions = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1))

def elves_around(elve):
  all_around = [tuple([elve[i]+ad[i] for i in range(2)]) for ad in all_directions]
  for a in all_around:
    if a in elves:
      return True
  return False

#checks if elve can move in proposed direction, e.g. for N checks for elves at (N, NW, NE)
def can_move_dir(elve, d):
  in_dir = [tuple([elve[i]+adj[i] for i in range(2)]) for adj in adj_directions[d]]
  # print(elve, d, in_dir)
  for tile in in_dir:
    if tile in elves:
      return tile, False
  return tile, True

def print_elves():
  min_x = min([elve[0] for elve in elves])
  max_x = max([elve[0] for elve in elves])
  min_y = min([elve[1] for elve in elves])
  max_y = max([elve[1] for elve in elves])
  for y in range(min_y, max_y+1):
    row = []
    for x in range(min_x, max_x+1):
      if (x,y) in elves:
        t = '#'
      else:
        t = '.'
      row.append(t)
    print(''.join(row))
  print()


def solve_1():
  first_dir = 0 # starts at N
  for _ in range(10):
    # print_elves()
    seen = set()
    forbidden = set()
    proposed_positions = {}
    for ei, elve in enumerate(elves):
      if not elves_around(elve):
        continue
      for di in range(4):
        d = (first_dir+di)%4 # loop through directions
        np, can_move = can_move_dir(elve, d)
        # print(cmd)
        if can_move:
          break
      if can_move:
        if np not in seen:
          seen.add(np)
          proposed_positions[ei] = np
        else:
          forbidden.add(np)

    # move them
    for k, v in proposed_positions.items():
      if v not in forbidden:
        elves[k] = v

    first_dir += 1

  min_x = min([elve[0] for elve in elves])
  max_x = max([elve[0] for elve in elves])
  min_y = min([elve[1] for elve in elves])
  max_y = max([elve[1] for elve in elves])

  count_open = 0
  for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
      if (x,y) not in elves:
        count_open += 1

  print(count_open)
  


def solve_2():
  first_dir = 0 # starts at N
  rc = 1
  while True:
    if rc % 10 == 0:
      print(rc)
    # print_elves()
    forbidden = set()
    seen = set()
    proposed_positions = {}
    for ei, elve in enumerate(elves):
      move = False
      if not elves_around(elve):
        continue
      for di in range(4):
        d = (first_dir+di)%4 # loop through directions
        np, can_move = can_move_dir(elve, d)
        # print(cmd)
        if can_move:
          move = True
          break
        else:
          seen.add(np)
      if move:
        pp = tuple([elve[i]+main_directions[d][i] for i in range(2)])
        if pp not in seen:
          seen.add(pp)
          proposed_positions[ei] = pp
        else:
          forbidden.add(pp)

    if len(proposed_positions.keys()) == 0:
      break

    # move them
    for k, v in proposed_positions.items():
      if v not in forbidden:
        elves[k] = v

    first_dir += 1
    rc += 1

  print(rc)

solve_1()
elves = get_elves()
solve_2()


    