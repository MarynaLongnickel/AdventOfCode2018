from urllib.request import urlopen
from pylab import *
import numpy as np
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2010/day10.txt').read().decode()
nums = np.reshape([int(i) for i in re.findall('-?\d+', data)], (-1,4))

dis = 200000

s = 0
sky = [[0 for i in range(80)] for j in range(20)]

for i in range(11000):
    
  minx, maxx = min([i[0] for i in nums]), max([i[0] for i in nums])
  miny, maxy = min([i[1] for i in nums]), max([i[1] for i in nums])
  
  mx = abs(maxx - minx)
  my = abs(maxy - miny)
  if min(mx, my) > dis:
    print(i-1)
    imshow(skyy)
    plt.show()
    break
  else: dis = min(mx, my)
    
  skyy = sky.copy()
  sky = [[0 for i in range(80)] for j in range(20)]
  
  for n in nums:
    n[0] += n[2]
    n[1] += n[3]
    
    if mx < 150:
      if n[0] - minx < len(sky[0]) and n[1] - miny < len(sky):
        sky[n[1] - miny][n[0] - minx] = 1
