# --- Day 2: Inventory Management System ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%202/day2.txt')

ids = [i.decode()[:-1] for i in data]

c2 = 0
c3 = 0

for i in ids:
  two = False
  three = False
  
  for j in set(i):
    if two and three: break
    if i.count(j) == 2 and not two:
      two = True
      c2 += 1
    elif i.count(j) == 3 and not three:
      three = True
      c3 += 1
      
print(c2*c3)

# ---------------------- PART 2 ------------------------

def findIds():
  for i in range(len(ids)):
    for j in range(i+1, len(ids)):
      c = 0
      for k in range(len(ids[i])):
        if ids[i][k] != ids[j][k]: c += 1
        if c > 1:
          c = 0
          break
      if c == 1:
        return ''.join([ids[i][k] for k in range(len(ids[i])) if ids[i][k] == ids[j][k]])
        
findIds()
