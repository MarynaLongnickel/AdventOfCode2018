players = 426
marbles = 72058

d = {}

circle = [0,1]
cur = 1
i = 2

while i <= marbles:
  
  if i%23 != 0:
    loc = (cur+2)%len(circle)
    circle.insert(loc, i)
    cur = loc
    
  else:
    if i%players not in d.keys():
      d[i%players] = 0
      
    d[i%players] += i  
    xi = (cur-7)%len(circle)
    rmvd = circle[xi]
    cur = xi
    
    d[i%players] += rmvd
    circle.remove(rmvd)
    
  i += 1
    
print(max(d.values()))
