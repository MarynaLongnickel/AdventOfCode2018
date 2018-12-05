# --- Day 5: Alchemical Reduction ---

from urllib.request import urlopen
import string

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%205/day5.txt')

for line in data: poly = line.decode()
poly = poly[:-1]
  
l = len(poly)
alphabet = string.ascii_lowercase

while True:
  for a in alphabet:
    poly = poly.replace(a + a.upper(), '')
    poly = poly.replace(a.upper() + a, '')
  if len(poly) == l:
    print(len(poly))
    break
  l = len(poly)
  
# ---------------------- PART 2 ------------------------

shortest = 100000  

for a in alphabet:
  poly2 = poly2.replace(a, '')
  poly2 = poly2.replace(a.upper(), '')
  
  l = len(poly2)

  while True:
    for a in alphabet:
      poly2 = poly2.replace(a + a.upper(), '')
      poly2 = poly2.replace(a.upper() + a, '')
    if len(poly2) == l:
      if len(poly2) < shortest:
        shortest = len(poly2)
      break
    l = len(poly2)
    
print(shortest)
