# --- Day 5: Alchemical Reduction ---

from urllib.request import urlopen
import string

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%205/day5.txt')

poly = data.read().decode()[:-1]
alphabet = string.ascii_lowercase
  
l = len(poly)

def reduce(arr):
  for a in alphabet:
    arr = arr.replace(a + a.upper(), '').replace(a.upper() + a, '')
  return arr

while True:
  poly = reduce(poly)
  if len(poly) == l:
    print(len(poly))
    break
  l = len(poly)
  
# ---------------------- PART 2 ------------------------

shortest = 100000  

for a in alphabet:
  poly2 = poly.replace(a, '').replace(a.upper(), '')
  
  l = len(poly2)

  while True:
    poly2 = reduce(poly2)
    if len(poly2) == l:
      if len(poly2) < shortest:
        shortest = len(poly2)
      break
    l = len(poly2)
    
print(shortest)
