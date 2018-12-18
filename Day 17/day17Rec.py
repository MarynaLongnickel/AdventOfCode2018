# super slow :(
# recursion is teh suck ...

import warnings
warnings.filterwarnings("ignore")

from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2017/day17.txt').read().decode().split('\n')[:-1]
coor = []

for d in data:
  nums = [int(i) for i in re.findall(r'\d+', d)]
  if d[0] == 'x':
    coor.extend([(nums[0], i) for i in range(nums[1], nums[2] + 1)])
  else:
    coor.extend([(i, nums[0]) for i in range(nums[1], nums[2] + 1)])
    
cx, cy = zip(*coor)
minx, maxx = min(cx), max(cx)
miny, maxy = min(cy), max(cy)

water = []
done = 0

def flow(water, pt):
  global done
  if done: return
  if pt not in water:
    water.append(pt)
  x,y = pt
  if y < maxy:
    while (x, y+1) not in coor:
      if y+1 > maxy:
        return 1
      water.append((x,y+1))
      y += 1
      
    collect(water, (x, y))


def collect(water, pt):
  global done
  if done: return
  x,y = pt
  if minx <= x <= maxx and y < maxy:
    i = x - 1
    j = x + 1

    while (i, y) not in coor:
      if (j, y) in water: return
      if y >= maxy: break
      if (i, y+1) in coor or (i, y+1) in water:
        if (i, y) not in water:
          water.append((i, y))
          i -= 1
      else:
        if flow(water, (i, y)): break
        
    while (j, y) not in coor:
      if (j, y) in water: return
      if y >= maxy: break
      if (j, y+1) in coor or (j, y+1) in water:
        if (j, y) not in water:
          water.append((j, y))
          j += 1
      else:
        done = flow(water, (j, y))
        if done: return
  
    collect(water, (x, y-1))
    
  flow(water, (500, 0))
