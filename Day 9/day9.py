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

# ---------------------- PART 2 ------------------------
# (also works for part 1)

class Node():
  def __init__(self, v = None, prev = None, next = None):
    self.v = v
    self.prev = prev
    self.next = next
    
  def remove(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    del self

def circle(players, marbles):
  
  p1 = Node(0)
  p2 = Node(1)
  p1.next = p2
  p1.prev = p2
  p2.next = p1
  p2.prev = p1
  cur = p2
  
  scores = {}
  
  for p in range(players):
    scores[p] = 0
  
  for i in range(2, marbles + 1):
    
    if i%23 != 0:
      cur = cur.next
      new = Node(i)
      
      cur.next.prev = new
      new.next = cur.next
      cur.next = new
      new.prev = cur
      cur = new
        
    else:
      for _ in range(7): cur = cur.prev
        
      scores[i%players] += i + cur.v
      
      tmp = cur.next
      cur.remove()
      cur = tmp
      
  print(max(scores.values()))
  
circle(426, 72058 * 100)
