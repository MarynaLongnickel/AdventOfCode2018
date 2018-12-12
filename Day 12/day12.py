from urllib.request import urlopen
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2012/day12.txt').read().decode().split('\n')

# keep track of how much the list gets shifted to the right as plants get close to the left side
added = 0
# set initial state (i replaced symbols so regex doesn't get confused)
init = data[0].replace('#', 'X').replace('.', 'o')
d = {}
s = 0

# fill in the states dictionary
for i in data[1:-1]:
  n1 = i[:5].replace('#', 'X').replace('.', 'o')
  n2 = i[-1].replace('#', 'X').replace('.', 'o')
  d[n1] = n2
  
# number of generations  
g = 300

for j in range(g):
  # get answer for part 1 after 20 generations
  if j == 20:
    for p in range(len(init)):
      if init[p] == 'X':
        s += p - added
    print(s)
  # if plants are spreading closer to the right or left edge, add more empty pots
  if 'X' in init[:4]:
    added += 5
    init = 'ooooo' + init
  if 'X' in init[-4:]:
    init = init + 'ooooo'
    
#   print(j, added, ''.join(['.' if i == 'o' else '#' for i in init]))
  
  # initialize empty array to keep track of changes of states for the current generation
  new = ['o' for _ in range(len(init))]
  
  # replace state with its corresponding value in dictionary
  for k in d.keys():
    ixs = [(m.span()) for m in re.finditer(k, init)]
    for i in re.finditer(r'(?=('+ k + '))', init):
      new[(i.start(1) + i.end(1))//2] = d[k]
      
  # collapse list of new pots and plants to a string
  new = ''.join(new)
  
  # if the state has reached a stable point (configuration of plants just moves around the pots, but remains the same)
  if 'o' + init == new + 'o':
    s = 0
    # find the new sum as the stable position
    for p in range(len(init)):
      if init[p] == 'X':
        s += p - added
    # count the number of plants
    c = init.count('X')
    # calculate what the sum of the configuration will be after 50000000000 generations
    print((5*(10**10) - j) * c + s)
    break
    
  # reset initial state to reflect changes that occured in current generation  
  init = new
