from urllib.request import urlopen
from copy import deepcopy

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2018/day18.txt').read().decode().split('\n')[:-1]
data = [list(d) for d in data]

maxr = len(data)
maxc = len(data[0])
x = {'.': '|', '|': '#'}

def around(r, c):
  w = data[r][c]

  if w in '.|':
    count = 0
    if r > 0:
      if data[r - 1][c] == x[w]: count += 1
    if r < maxr - 1:
      if data[r + 1][c] == x[w]: count += 1
    if c > 0:
      if data[r][c - 1] == x[w]: count += 1
    if c < maxc - 1:
      if data[r][c + 1] == x[w]: count += 1
    if r > 0 and c > 0:
      if data[r - 1][c - 1] == x[w]: count += 1
    if r < maxr - 1 and c < maxc - 1:
      if data[r + 1][c + 1] == x[w]: count += 1
    if c > 0 and r < maxr - 1:
      if data[r + 1][c - 1] == x[w]: count += 1
    if c < maxc - 1 and r > 0:
      if data[r - 1][c + 1] == x[w]: count += 1
    if count > 2:
      return x[w]
      
  elif w == '#':
    count_t = 0
    count_l = 0
    if r > 0:
      if data[r - 1][c] == '|': count_t += 1
      if data[r - 1][c] == '#': count_l += 1
    if r < maxr - 1:
      if data[r + 1][c] == '|': count_t += 1
      if data[r + 1][c] == '#': count_l += 1
    if c > 0:
      if data[r][c - 1] == '|': count_t += 1
      if data[r][c - 1] == '#': count_l += 1
    if c < maxc - 1:
      if data[r][c + 1] == '|': count_t += 1
      if data[r][c + 1] == '#': count_l += 1
    if r > 0 and c > 0:
      if data[r - 1][c - 1] == '|': count_t += 1
      if data[r - 1][c - 1] == '#': count_l += 1
    if r < maxr - 1 and c < maxc - 1:
      if data[r + 1][c + 1] == '|': count_t += 1
      if data[r + 1][c + 1] == '#': count_l += 1
    if c > 0 and r < maxr - 1:
      if data[r + 1][c - 1] == '|': count_t += 1
      if data[r + 1][c - 1] == '#': count_l += 1
    if c < maxc - 1 and r > 0:
      if data[r - 1][c + 1] == '|': count_t += 1
      if data[r - 1][c + 1] == '#': count_l += 1
    if count_t == 0 or count_l == 0:
      return '.'
    
  return w
  
totals = []
prev = 0
prev2 = 0

for i in range(1000000000):
  if i%1000 == 0: print(i)
  new = deepcopy(data)
  t = 0
  l = 0
  
  for r in range(maxr):
    for c in range(maxc):
      new[r][c] = around(r, c)
      if new[r][c] == '|': t += 1
      elif new[r][c] == '#': l += 1
        
  tot = t * l
  
  # see if the pattern started again by checking if the last two numbers appear consecutively in the list
  if tot in totals and prev == totals[totals.index(tot) - 1] and prev2 == totals[totals.index(tot) - 2]: break 
  else: prev, prev2 = tot, prev
    
  totals.append(tot)
  data = deepcopy(new)
  
N = 1000000000
end = totals.index(prev) - 1
pattern = len(totals) - 2 - end
ix = end + (N - end - 1) % pattern

print(totals[ix])
