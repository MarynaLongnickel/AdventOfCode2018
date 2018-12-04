# --- Day 3: No Matter How You Slice It ---

from urllib.request import urlopen
import numpy as np

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/RandomStuff/master/Advent%20of%20Code%202018/day3.txt')
patches = [['.' for _ in range(1000)] for _ in range(1000)]

count = 0
i = 0

squares = []

for line in data:
  # parse each line to extract the four numbers
  i += 1
  if i < 10: line = line[5:-2].decode()
  elif i < 100: line = line[6:-2].decode()
  elif i < 1000: line = line[7:-2].decode()
  elif i < 1401: line = line[8:-2].decode()
  else: line = line[8:].decode()
    
  line = line.replace(': ', ',')
  line = line.replace('x', ',')
  line = line.replace(' ', '')
  line = line.split(',')
  line = [int(i) for i in line]
  
  # append areas of each claim to use in part two
  squares.append(line[2]*line[3])
  
  # fill out the patches matrix with all the claims
  for n in range(line[1], line[1] + line[3]):
    for m in range(line[0], line[0] + line[2]):
      if patches[n][m] == '.':
        patches[n][m] = i
      elif patches[n][m] not in ['O', '.']:
        count += 1
        patches[n][m] = 'O'
      
print(count)

# ---------------------- PART 2 ------------------------

# count how many non-overlapping square inches of each claim are left

p = np.array(patches)
areas = np.unique(p, return_counts=True)
areas = dict(list(zip(*areas))[1:-1])

# compare the number of left over non-overlapping squares to the areas of the
# corresponding claims.
# when the numbers are equal that claim is completely uncovered by others

for i in range(len(squares)):
  if str(i+1) in areas.keys():
    if areas[str(i+1)] == squares[i]:
      print(i + 1)
