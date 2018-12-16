from skimage.graph import route_through_array as RTA
from scipy.spatial.distance import cityblock as CB
from urllib.request import urlopen
from operator import itemgetter
import numpy as np
from copy import deepcopy

notes = False

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2015/day15.txt').read().decode().split('\n')

for i in range(len(data)): data[i] = list(data[i])
data = data[:-1]

j = 0
units = {}
infi = 10**6
U = 10**3


print(np.matrix(data))
  
for r in range(len(data)):
  for c in range(len(data[0])):
    if data[r][c] == '.':
      data[r][c] = 1
    elif data[r][c] == 'E':
      units[j] = [j, 'E', 200, r, c]
      data[r][c] = U
      j += 1
    elif data[r][c] == 'G':
      units[j] = [j, 'G', 200, r, c]
      data[r][c] = U
      j += 1
    else:
      data[r][c] = infi
        

d = {'E': 'G', 'G': 'E'}
over = False

for m in range(100):
  if notes: print(m,'='*60)
  if over:
    print(m-1, sum([v[2] for v in units.values()]), (m-1) * sum([v[2] for v in units.values()]))
    break
  units2 = deepcopy(units)
  data2 = [x[:] for x in data]
  
  order = sorted(list(units.values()), key=itemgetter(3,4))

  for u in [o[0] for o in order]:
    attack = False

    W = units[u][1]
    r = units[u][3]
    c = units[u][4]

    move = []
    closest = None
    kill = None
    dis = infi

    targets = [(x[0], [x[3], x[4]]) for x in list(units.values()) if x[1] == d[W]]
    if not targets:
      over = True
      break
      
    for t in targets:
      if t[0] not in units.keys(): continue
      path = RTA(data, [r, c], t[1], fully_connected=False)
      if path[1] == U:
        if kill is None: kill = t[0]
        if units[t[0]][2] < units[kill][2]:
          kill = t[0]
        elif (units[t[0]][2] == units[kill][2]) and (t[1][0] * len(data[0]) + t[1][1]) < (units[kill][3] * len(data[0]) + units[kill][4]):
          kill = t[0]
            
        attack = True
        
      elif path[1] < dis:
        if dis == infi:
          dis = path[1]
        if not move:
          move = path[0][1]
          closest = t[0]
        if data[path[0][1][0]][path[0][1][1]] < U:
          dis = path[1]
          move = path[0][1]
          closest = t[0]
          
      elif path[1] == dis:
        if data[path[0][1][0]][path[0][1][1]] < U and move > path[0][1]:
          move = path[0][1]
          closest = t[0]

        
    if attack:
      units2[kill][2] -= 3
      if units2[kill][2] < 1:
        data2[units[kill][3]][units[kill][4]] = 1
        del units2[kill]
        del units[kill]
        if len(list(set([x[1] for x in units.values()]))) == 1:
          over = True
          break

    elif dis == U*2: continue

    else:
      r2, c2 = move
      if (r2, c2) in [(x[3],x[4]) for x in units2.values()]: continue
      if data[r2][c2] != U:
        data2[r][c] = 1
        data2[r2][c2] = U
        units2[u][3] = r2
        units2[u][4] = c2
        data[r][c] = 1
        data[r2][c2] = U
        units[u][3] = r2
        units[u][4] = c2
       
      if CB([r2, c2], units[closest][3:]) == 1:
        units2[closest][2] -= 3
        if units2[closest][2] < 1:
          data2[units[closest][3]][units[closest][4]] = 1
          del units2[closest]
          del units[closest]
          if d[d[W]] not in units2.keys():
            over = True
            break
            
  data = [x[:] for x in data2]
  units = deepcopy(units2)
