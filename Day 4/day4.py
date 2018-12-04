# --- Day 4: Repose Record ---

from urllib.request import urlopen
from collections import Counter
import pandas as pd
import numpy as np

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/RandomStuff/master/Advent%20of%20Code%202018/Day%204/day4.txt')

df = []

# parse each line to extract timestamp, guard ID, and whether they are asleep
for line in data:
  line = line[1:-1].decode()
  line = line.replace(']', '')
  line = line.split(' ')
  line[1] = line[0] + ' ' + line[1]
  line = line[1:]
  if line [1] == 'wakes':
    line = [line[0], 'U']
  if line [1] == 'falls':
    line = [line[0], 'S']
  if line [1] == 'Guard':
    line = [line[0], line[2][1:]]
  df.append(line)
  
# convert data to DataFrame and sort by timestamp
df = pd.DataFrame(df)
df = df.sort_values(by = [0])

dates = list(df[0])
l = list(df[1])

# guards dictionary will contain all the minutes a guard asleep
guards = {}
g = None
i = 0

# populate the guards dictionary
while i < len(l):
  x = l[i]
  if x not in ['U', 'S']:
    if x not in guards.keys():
      guards[x] = []
    g = x
  elif x == 'S':
    guards[g].extend(range(int(dates[i][-2:]), int(dates[i+1][-2:])))
    i += 1
  i += 1
  
total = 0
minute = 0
guard = None

# count the total number of minutes each guard slept and find the largest
for i in guards.keys():
  l = len(guards[i])
  if l > total:
    total = l
    c = Counter(guards[i]).most_common()[0]
    minute = c[0]
    guard = int(i)
    
print(guard, minute, ': ', guard * minute)

# ---------------------- PART 2 ----------------------

total = 0
minute = 0
guard = None


# find which minute a guard slept the most
for i in guards.keys():
  c = Counter(guards[i]).most_common()
  if len(c) > 0:
    c = c[0]
    if c[1] > total:
      minute = c[0]
      total = c[1]
      guard = int(i)
    
print(guard, minute, ': ', guard * minute)
