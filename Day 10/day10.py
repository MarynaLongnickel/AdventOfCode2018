from urllib.request import urlopen
from pylab import *
import numpy as np
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2010/day10.txt').read().decode()
nums = np.reshape([int(i) for i in re.findall('-?\d+', data)], (-1,4))

w, h, dis = 80, 20, 200000
sky = [[0 for i in range(w)] for j in range(h)]

for i in range(11000):
    
  minx, maxx = min([i[0] for i in nums]), max([i[0] for i in nums])
  miny, maxy = min([i[1] for i in nums]), max([i[1] for i in nums])
  
  mx, my = abs(maxx - minx), abs(maxy - miny)
  
  if min(mx, my) > dis:
    print(i-1)
    break
  else: dis = min(mx, my)
    
  skyy = sky.copy()
  sky = [[0 for i in range(80)] for j in range(20)]
  
  for n in nums:
    n[0] += n[2]
    n[1] += n[3]
    
    if mx < 150 and n[0] - minx < w and n[1] - miny < h:
      sky[n[1] - miny][n[0] - minx] = 1
        
imshow(skyy);
