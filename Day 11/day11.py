import numpy as np

d = 300
grid = np.zeros((d,d))
sn = 3613

for r in range(d):
  for c in range(d):
    fuel = ((c + 10)*r + sn)*(c + 10)
    if fuel > 99: fuel = int(str(fuel)[-3]) - 5
    else: fuel = -5
    grid[r][c] = fuel
 
m = 0  
tl = (0,0)
ms = 0

for s in range(d):
  for r in range(d - s + 1):
    c = 0
    square = grid[r:r + s, c:c + s]
    p = np.matrix(square).sum()
    for c in range(d - s):
      if p > m:
        m = p
        ms = s
        tl = (c, r)
      p -= grid[r:r + s, c].sum()
      p += grid[r:r + s, c + s].sum()

if p > m:
  m = p
  ms = s
  tl = (c, r)
  
print(tl[0], tl[1], ms)
