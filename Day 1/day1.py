# --- Day 1: Chronal Calibration ---

from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/Advent-of-Code-2018/master/Day%201/day1.txt')
nums = []

for n in data:
  n = n.decode()
  if n[0] == '+': nums.append(int(n[1:]))
  else: nums.append(-int(n[1:]))
    
sum(nums)

# ---------------------- PART 2 ------------------------

s = set()

found = False
f = 0

while not found:
  for i in nums:
    f += i
    if f in s:
      found = True
      print(f)
      break
    s.add(f)
