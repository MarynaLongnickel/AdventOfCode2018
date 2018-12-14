class Node():
  def __init__(self, v = None, next = None):
    self.v = v
    self.next = next

e1, e2 = Node(3), Node(7)

e1.next = e2
e2.next = e1

start = e1
cur = e2

num = '409551'
n = 0
count = 2
recepies = []

done = False

while not done:    
  r = list(map(int,str(e1.v + e2.v)))
  
  for i in r:
    new = Node(i)
    cur.next = new
    cur = new
    count += 1
    if cur.v == int(num[n]):
      recepies.append(cur.v)
      n += 1
      if n == len(str(num)):
        done = True
        print(count - len(num))
        break
    elif cur.v == int(num[0]):
        recepies = [cur.v]
        n = 1
    else:
      recepies = []
      n = 0

  if done: break   
    
  cur.next = start

  for _ in range(1 + e1.v): e1 = e1.next
  for _ in range(1 + e2.v): e2 = e2.next
      
   
  if count == int(num) + 10 + 1:
    arr = []
    x = start
    for z in range(count):
      if z >= int(num) and len(arr) < 10:
        arr.append(x.v)
      x = x.next
    print(arr)  
