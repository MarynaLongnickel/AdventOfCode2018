from urllib.request import urlopen
from operator import itemgetter

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2013/day13.txt').read().decode().split('\n')

# convert data into a 2d array
for i in range(len(data)): data[i] = list(data[i])
  
j = 0
carts = {}
dir = {'>': ['^', 'v'], '<': ['v', '^'], '^': ['<', '>'], 'v': ['>', '<']}

# find all carts and set their initial states, then remove from map and replace with track
def clean(r,c):
  global j
  for a in ['^', '>', 'v', '<']:
    if data[r][c] == a:
      data[r][c] = '|' if a in ['^', 'v'] else '-'
      carts[j] = [j, a, 'l', r, c]
      j += 1
      return

# remove carts that have crashed and check if there's only one left
def isLast(j):
  if carts[j][3:] in loc:
    if len(carts) == 17: print(carts[j][3:])
    for m in carts.keys():
      # if carts moves into position that's already occupied, there's a crash
      if carts[m][3:] == carts[j][3:] and m != j:
        del carts[m]
        del carts[j]
        if len(carts) == 1:
          print(list(carts.values())[0][3:])
        break
    
# update cart's position
def move(j, r, c):
  for a in ['^', '>', 'v', '<']:
    if carts[j][1] == a:
      r2 = 0 if a in ['<', '>'] else -1 if a == '^' else 1
      c2 = 0 if a in ['^', 'v'] else -1 if a == '<' else 1
      
      if data[r + r2][c + c2] == '\\': carts[j][1] = dir[a][1] if a in ['<', '>'] else dir[a][0]
      elif data[r + r2][c + c2] == '/': carts[j][1] = dir[a][0] if a in ['<', '>'] else dir[a][1]
      elif data[r + r2][c + c2] == '+':
        
        # direction in which the cart moves at an intersection
        if carts[j][2] == 'l':
          carts[j][1] = dir[a][0]
          carts[j][2] = 's'
        elif carts[j][2] == 's':
          carts[j][2] = 'r'
        elif carts[j][2] == 'r':
          carts[j][1] = dir[a][1]
          carts[j][2] = 'l'  
          
      carts[j][4 if a in ['<', '>'] else 3] += 1 if a in ['v', '>'] else -1
      isLast(j)
      break
    
    
for r in range(len(data)):
  for c in range(len(data[r])):
    clean(r,c)
    
    
for i in range(100000):
  if len(carts) == 1: break
   
  # get the order in which the carts move based on their location
  order = sorted(list(carts.values()), key=itemgetter(3,4))
  
  for j in [o[0] for o in order]:
    # get locations of remaining carts
    loc = [carts[i][3:] for i in carts.keys()]
    
    if j not in carts.keys(): continue
    r = carts[j][3]
    c = carts[j][4]
    
    move(j, r, c)
