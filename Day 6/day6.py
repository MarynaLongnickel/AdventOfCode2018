from scipy.spatial.distance import cityblock
from urllib.request import urlopen
import numpy as np

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%206/day6.txt')

coor = []

# parse data and fill in the grid with given coordinates
for line in data:
  line = line.decode()[:-1]
  line = line.replace(' ', '')
  line = line.split(',')
  coor.append([int(line[0]),int(line[1])])
  
  
# find minimum dimensions of the grid to contain all coordinates
dim = max(map(max, coor)) + 1 
# initialize matrix to hold each location's closest coordinate
m = [['.' for _ in range(dim)] for _ in range(dim)] 


# initialize area variable for Part 2
area = 0

# fill in the matrix with closest coordinates
for r in range(dim):
  for c in range(dim):
    same = False
    ds = []
    for n in coor:
      d = cityblock([r,c], n)
      ds.append(d)
    if sum(ds) < 10000: area += 1
    if ds.count(min(ds)) < 2:
      m[r][c] = ds.index(min(ds))
      
# tally up the number of locations closest to each coordinate
counts = dict(zip(*np.unique(np.array(m).ravel(), return_counts=True)))
del counts['.']

# get indices of coordinates corresponding to infinite areas (around the edges of matrix)
infi = []
infi.extend(np.unique(m[0]))
infi.extend(np.unique(m[-1]))
infi.extend(np.unique([m[i][-1] for i in range(dim)]))
infi.extend(np.unique([m[i][0] for i in range(dim)]))
infi = np.unique(infi)
infi = infi[1:]

# find the largest area

largest = 0

for i in counts.keys():
  if i not in infi and counts[i] > largest:
    largest = counts[i]
    
print(largest)

# ---------------------- PART 2 ------------------------
      
print(area)
