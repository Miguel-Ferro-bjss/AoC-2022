from collections import deque

# DISCLAIMER: this solution is painstakingly hardocoded to fit my input

def parse_input(part=1, test = False):

  if not test:
    f = open('input.txt', 'r').read().split('\n')
  else:
    f = open('test.txt', 'r').read().split('\n')

  l = 0
  for line in f[0:-2]:
    l = max(l, len(line))

  grid = []

  for line in f[0:-2]:

    if part == 2:
      line = line.replace(' ', '')

    row = []

    if part == 1:
      for i in range(l):
        if i < len(line):
          tile = line[i]
        else:
          tile = '-'
        if tile == ' ': row.append('-')
        else: row.append(tile)
      grid.append(row)

    if part == 2:
      grid.append([t for t in line])

  raw_instructions = f[-1]

  num = []
  inst = []
  digits = '0123456789'
  for i, ri in enumerate(raw_instructions):
    if ri in digits:
      num.append(ri)
    else:
      if num:
        if len(num) > 1:
          inst.append(int(''.join(num)))
        else:
          inst.append(int(num[0]))
        num = []
      inst.append(ri)
  if num:
    if len(num) > 1:
      inst.append(int(''.join(num)))
    else:
      inst.append(int(num[0]))

  return grid, inst

#input cube
#.12
#.3.
#45.
#6..

#test cube
#..1.
#234.
#..56

def parse_cube(test=False):

  grid, inst = parse_input(part=2)
  # print(grid)

  if test:
    face_length = 4
  else:
    face_length = len(grid[0])//2
  face_num = len(grid) // face_length
  # print('face lenght:', face_length)
  # print('face num:', face_num)

  faces = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []} # each face will be a 2D grid, key is the face number

  if test:
    return faces
  
  faces_per_row = len(grid[0]) // face_length
  completed_faces = 0
  for i, row in enumerate(grid):
    # print(i, row)
    if len(row) // face_length != faces_per_row:
      completed_faces += faces_per_row
      faces_per_row = len(row) // face_length
    r = []
    face_increment = 1
    for j, t in enumerate(row):
      r.append(t)
      if j in [50*i - 1 for i in range(1,4)]:
        faces[completed_faces + face_increment].append(r)
        r = []
        face_increment += 1
      
      
  return faces, inst

def next_tile(pos, d, grid):

  l = len(grid[0])
  new_pos = pos
  while(True):
    new_pos = tuple([new_pos[i] + d[i] for i in range(2)])
    new_pos = (new_pos[0]%l, new_pos[1]%len(grid))
    if grid[new_pos[1]][new_pos[0]] == '.':
      return new_pos, False
    if grid[new_pos[1]][new_pos[0]] == '#':
       return pos, True
    if grid[new_pos[1]][new_pos[0]] == '-':
      continue

directions = ((1,0), (0,1), (-1,0), (0,-1))

def next_tile_cube(pos, faces, test=False):
  if not test:
    # mapping each face (key) edge (r, d, l, u) to each face (face, dir)
    wrapping = {
      1: ((2, 0), (3, 1), (4, 0), (6, 0)),
      2: ((5, 2), (3, 2), (1, 2), (6, 3)),
      3: ((2, 3), (5, 1), (4, 1), (1, 3)),
      4: ((5, 0), (6, 1), (1, 0), (3, 0)),
      5: ((2, 2), (6, 2), (4, 2), (3, 3)),
      6: ((5, 3), (2, 1), (1, 1), (4, 3))
    }
    coord_flip = {
      1: {4: lambda x, y: (0,-y-1), 6: lambda x,y: (0,x), 2: lambda x,y: (0,y), 3: lambda x,y: (x,0)},
      2: {1: lambda x,y: (-1,y), 3: lambda x,y: (-1,x), 5: lambda x,y: (-1,-y-1), 6: lambda x,y: (x,-1)},
      3: {1: lambda x,y: (x,-1), 4: lambda x,y: (y,0), 2: lambda x,y: (y,-1), 5: lambda x,y: (x,0)},
      4: {1: lambda x,y: (0,-y-1), 3: lambda x,y: (0,x), 5: lambda x,y: (0,y), 6: lambda x,y: (x,0)},
      5: {3: lambda x,y: (x,-1), 2: lambda x,y: (-1,-y-1), 4: lambda x,y: (-1,y), 6: lambda x,y: (-1,x)},
      6: {1: lambda x,y: (y,0), 4: lambda x,y: (x,-1), 5: lambda x,y: (y,-1), 2: lambda x,y: (x,0)}
    }
  # pos = (x , y, d_i, face)
  d_i = pos[2]
  d = directions[d_i]
  f = pos[3]

  grid = faces[f]
  x_max, y_max = len(grid[pos[1]]), len(grid)  
  
  
  nx, ny = pos[0] + d[0], pos[1] + d[1]
  
  if nx < 0 or nx >= x_max or ny < 0 or ny >= y_max:
    w = wrapping[f][d_i]
    nf, d_i = w[0], w[1]
    nx, ny = coord_flip[f][nf](nx, ny)
    nx, ny = nx%x_max, ny%y_max
    grid = faces[nf]
    f = nf
  if grid[ny][nx] == '.':
    return (nx, ny, d_i, f), False
  elif grid[ny][nx] == '#':
    return pos, True

    

def solve_1():

  grid, inst = parse_input(1)

  instructions = deque(inst)
  d_i = 0
  d = directions[d_i]

  pos, _ = next_tile((0,0), d, grid)

  while(instructions):
    inst = instructions.popleft()
    # print(pos, inst, d_i)
    if type(inst) == int:
      for _ in range(inst):
        pos, wall = next_tile(pos, directions[d_i], grid)
        if wall: break
    else:
      if inst == 'R':
        d_i = (d_i + 1) % 4
      elif inst == 'L':
        d_i = (d_i - 1) % 4

  # print(pos[1]+1, pos[0]+1, d_i)
  print('part 1:', 1000*(pos[1]+1) + 4*(pos[0]+1) + d_i)

def cube_to_grid(pos):
  x,y,d,f = pos
  f2g = {1: (50,0), 2: (100,0), 3: (50,50), 4: (0,100), 5: (50,100), 6: (0,150)}
  dx, dy = f2g[f]

  return x+dx, y+dy, d, f
  


def solve_2():

  faces, inst = parse_cube()
  instructions = deque(inst)
  pos = (0,0,0,1) # (x, y, d_i, f)

  while(instructions):
    # print(cube_to_grid(pos))
    inst = instructions.popleft()
    # print(pos, inst)
    if type(inst) == int:
      for _ in range(inst):
        # print(next_tile_cube(pos, faces))
        pos, wall = next_tile_cube(pos, faces)
        if wall: break
    else:
      d_i = pos[2]
      if inst == 'R':
        d_i = (d_i + 1) % 4
      elif inst == 'L':
        d_i = (d_i - 1) % 4
      pos = (pos[0], pos[1], d_i, pos[3])
    # print(pos)
  grid_pos = cube_to_grid(pos)

  # print(pos[1]+1, pos[0]+1, d_i)
  print('part 2:', 1000*(grid_pos[1]+1) + 4*(grid_pos[0]+1) + d_i)

solve_1()
solve_2()