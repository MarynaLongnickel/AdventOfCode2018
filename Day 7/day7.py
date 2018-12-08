from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%207/day7.txt')

steps = []

# parse data to extract the two letters
for line in data:
  line = line.decode()
  line = line.split(' ')
  steps.append([line[1], line[7]])
  
# save a copy for part 2
steps2 = steps.copy()
  
# lists of source and destination letters
first = set([i[0] for i in steps])
second = set([i[1] for i in steps])

# staring and ending letters
start = sorted(list(first - second))[0]
end = sorted(list(second - first))[-1]

next = [i[1] for i in steps if i[0] == start]
next.extend(sorted(list(first - second))[1:])
# list of letters without a source and destinations of first letter
next = sorted(next)
# remove entries with source as first letter as it has been seen
steps = [i for i in steps if i[0] != start]

order = [start]
s = sorted(next)
l = 0

while s:
  if l == len(s):  l = 0
    
  next = [i[1] for i in steps if i[0] == s[l]]
  complete = list(set([i[1] for i in steps]))
  
  if s[l] not in complete:
    order.append(s[l])
    # remove entries with source as s[l] as it has been seen
    steps = [i for i in steps if i[0] != s[l]]
    s.remove(s[l])
    s.extend(next)
    s = sorted(list(set(s)))
    l = 0
    
  else:
    s.extend(next)
    s = sorted(list(set(s)))
    l += 1
    
''.join(order)


# ---------------------- PART 2 ------------------------

steps = steps2

# collect all letters
all = list(first)
all.extend(list(second))
all = list(set(all))

# create dictionary with letters as keys and lists of sources as values
d = {}
for i in all: d[i] = [j[0] for j in steps if j[1] == i]
  
# number of workers
N = 5
# seconds per task
s = 60  
  
# get starting letters (ones without a source)  
next = sorted([[ord(k) - 65 + s, k] for k in d.keys() if d[k] == []])
# queue lettes if there are more than workers
Q = [n[1] for n in next[N:]]
next = dict(next)

seen = []
time = 0

while len(seen) < len(all):
  
  # letters currently being worked on
  working = [n[1] for n in next.items() if n[0] >= s]
  
  # if letter tast has been completed
  if time in next.keys():
    # if two tasks end at the same time, unpack the list and append to seen
    if type(next[time]) == list:
      seen.extend(next[time])
      seen = sorted(seen)
    else:
      seen.append(next[time])
    # remove completed task
    del next[time]

    new = []
    # see which new letters are now available
    for k in d.keys():
      if set(d[k]).issubset(seen) and k not in next.values():
        if k not in seen:
          new.append(k)
    
    # if not all workers are busy
    if len(next.keys()) <= N:
      
      # first take tasks from queue
      if Q:
        for q in Q:
          x = ord(q) - 65 + time + 1 + s
          next[x] = q
          Q.remove(q)
          if len(next.keys()) == N: break

      else:
        for n in sorted(new):
          x = ord(n) - 65 + time + 1 + s
          
          if len(next.keys()) == N:
            if n not in Q:
              Q.append(n)
            
          elif n not in next.values() and (not any(n in v for v in next.values())):
            if x in next.keys():
              next[x] = [next[x], n]
            else:
              next[x] = n
   
  time += 1
  
print(time)
