f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')

cubes = set()
for line in f:
  x, y ,z = [int(p) for p in line.split(',')]
  cubes.add((x, y, z))

shell = [(-1,0,0), (0,-1,0), (0,0,-1), (1,0,0), (0,1,0), (0,0,1)]
ext = []
area = 6*len(cubes)
adj = set()
for c in cubes:
  for s in shell:
    cc = (c[0]+s[0], c[1]+s[1], c[2]+s[2])
    if cc in cubes:
      area += -1
    else:
      ext.append(cc)

print('part 1:', area)

edges = [[min(cube[d] for cube in cubes) for d in range(3)], [max(cube[d] for cube in cubes) for d in range(3)]]

def propagate_neighbors(point):
    neighbours = set()
    to_check = [point]
    while to_check:
        curr_point = to_check.pop()
        if curr_point in cubes:
          continue
        for i,s in enumerate(shell):
          p = tuple([curr_point[d] + s[d] for d in range(3)])
          if (i<3 and p[i] < edges[0][i]) or (i>2 and edges[1][i-3] < p[i-3]):
              return True
          if p not in neighbours:
              neighbours.add(p)
              to_check.append(p)

    air_pockets.update(neighbours)
    return False

air_pockets = set()

for c in ext:
  # print()
  if c in air_pockets or not propagate_neighbors(c):
    area += -1
  
print('part 2', area)