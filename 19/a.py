import re
from collections import deque

f = open('input.txt', 'r').read().strip().split('\n')
# f = open('test.txt', 'r').read().strip().split('\n')

blueprints = []
for line in f:
  numbers = re.findall('([0-9]+)', line)
  bp = {}
  bp = {}
  bp['ore'] = (int(numbers[1]), 0, 0, 0)
  bp['clay'] = (int(numbers[2]), 0, 0, 0)
  bp['obs'] = (int(numbers[3]), int(numbers[4]), 0, 0)
  bp['geode'] = (int(numbers[5]), 0, int(numbers[6]), 0)
  blueprints.append(bp)

def optimum_geode(bp, time):
  # print(bp)
  check = deque([(0, 0, 0, 0, 1, 0, 0, 0, 0)])
  geode = 0
  seen = set()

  ore_cap = max([bp[k][0] for k in bp])
  clay_cap = bp['obs'][1]
  obs_cap = bp['geode'][2]

  while check:
    ore, clay, obs, geo, r_ore, r_clay, r_obs, r_geo, t = check.popleft()
    geode = max(geode, geo)

    if t == time:
      continue
    
    if r_ore > ore_cap:
      r_ore = ore_cap
    if r_clay > clay_cap:
      r_clay = clay_cap
    if r_obs > obs_cap:
      r_obs = obs_cap

   
    if ore > (time-t) * ore_cap - r_ore * (time-t-1):
      ore = (time-t) * ore_cap - r_ore * (time-t-1)
    if clay > (time-t) * clay_cap - r_clay * (time-t-1):
      clay = clay_cap
    if obs > (time-t) * obs_cap - r_obs * (time-t-1):
      obs = (time-t) * obs_cap - r_obs * (time-t-1)
    
    if (ore, clay, obs, geo, r_ore, r_clay, r_obs, r_geo, t) in seen:
      continue
    seen.add((ore, clay, obs, geo, r_ore, r_clay, r_obs, r_geo, t))

    check.append((ore+r_ore, clay+r_clay, obs+r_obs, geo+r_geo, r_ore, r_clay, r_obs, r_geo, t+1))

    if ore >= bp['ore'][0]:
      check.append((ore + r_ore - bp['ore'][0], clay + r_clay, obs + r_obs, geo + r_geo, r_ore + 1, r_clay, r_obs, r_geo, t+1))

    if ore >= bp['clay'][0]:
      check.append((ore + r_ore - bp['clay'][0], clay + r_clay, obs + r_obs, geo + r_geo, r_ore, r_clay + 1, r_obs, r_geo, t+1))

    if ore >= bp['obs'][0] and clay >= bp['obs'][1]:
      check.append((ore + r_ore - bp['obs'][0], clay + r_clay - bp['obs'][1], obs + r_obs, geo + r_geo, r_ore, r_clay, r_obs + 1, r_geo, t+1))

    if ore >= bp['geode'][0] and obs >= bp['geode'][2]:
      check.append((ore + r_ore - bp['geode'][0], clay + r_clay, obs + r_obs - bp['geode'][2], geo + r_geo, r_ore, r_clay, r_obs, r_geo + 1, t+1))

  return geode


quality = 0
for i, bp in enumerate(blueprints):
  og = optimum_geode(bp, 24)
  quality += (i+1) * og

print('part 1: ', quality)

prod = 1
for i, bp in enumerate(blueprints[0:3]):
  og = optimum_geode(bp, 32)
  print(og)
  prod *= og

print('part 2: ', prod)