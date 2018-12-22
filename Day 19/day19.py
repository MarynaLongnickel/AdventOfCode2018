from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2019/day19.txt').read().decode().split('\n')[:-1]

# opcodes  
def addr(R, i): return [R[r] if r != i[2] else R[i[0]] + R[i[1]] for r in range(6)]
def addi(R, i): return [R[r] if r != i[2] else R[i[0]] + i[1] for r in range(6)]
def mulr(R, i): return [R[r] if r != i[2] else R[i[0]] * R[i[1]] for r in range(6)]
def muli(R, i): return [R[r] if r != i[2] else R[i[0]] * i[1] for r in range(6)]
def banr(R, i): return [R[r] if r != i[2] else R[i[0]] & R[i[1]] for r in range(6)]
def bani(R, i): return [R[r] if r != i[2] else R[i[0]] & i[1] for r in range(6)]
def borr(R, i): return [R[r] if r != i[2] else R[i[0]] | R[i[1]] for r in range(6)]
def bori(R, i): return [R[r] if r != i[2] else R[i[0]] | i[1] for r in range(6)]
def setr(R, i): return [R[r] if r != i[2] else R[i[0]] for r in range(6)]
def seti(R, i): return [R[r] if r != i[2] else i[0] for r in range(6)]
def gtir(R, i): return [R[r] if r != i[2] else 1 if i[0] > R[i[1]] else 0 for r in range(6)]
def gtri(R, i): return [R[r] if r != i[2] else 1 if R[i[0]] > i[1] else 0 for r in range(6)]
def gtrr(R, i): return [R[r] if r != i[2] else 1 if R[i[0]] > R[i[1]] else 0 for r in range(6)]
def eqir(R, i): return [R[r] if r != i[2] else 1 if i[0] == R[i[1]] else 0 for r in range(6)]
def eqri(R, i): return [R[r] if r != i[2] else 1 if R[i[0]] == i[1] else 0 for r in range(6)]
def eqrr(R, i): return [R[r] if r != i[2] else 1 if R[i[0]] == R[i[1]] else 0 for r in range(6)]


X = int(data[0][-1])

data = [d.split(' ') for d in data[1:]]
data = [[eval(d[0]), [int(i) for i in d[1:]]] for d in data]

ip = 0
inst = {}
R = [0 for _ in range(6)]
R[0] = 1

for i in range(len(data)): inst[i] = data[i]


j = 0

start = True
j = 0

while ip < len(data):
  if j%1000000 == 0: print(j, ip, R)
  if start:
    start = False
    R[0] = 1
  else: R[X] = ip
#   print('-'*130, R)
  f, n = inst[ip]
#   print('f: ', f.__name__, 'n: ', n)
  R = f(R, n)
  ip = R[X] + 1
#   print()
#   print('ip:', ip, 'R: ', R)
  j += 1
  
print(R[0])
