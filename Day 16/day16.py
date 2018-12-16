from urllib.request import urlopen
import ast

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2016/day16.txt').read().decode().split('\n\n')
nums = []

# parse data into the form [[before], (instructions), [after]].
for d in data:
  d = d.replace('Before: ', '').replace('\nAfter:  ', '').replace('\n', '')
  nums.append([ast.literal_eval(d[:12]), ast.literal_eval(d[12:-12].replace(' ', ',')), ast.literal_eval(d[-12:])])

# opcodes  
def addr(R, i): return [R[r] if r != i[3] else R[i[1]] + R[i[2]] for r in range(4)]
def addi(R, i): return [R[r] if r != i[3] else R[i[1]] + i[2] for r in range(4)]
def mulr(R, i): return [R[r] if r != i[3] else R[i[1]] * R[i[2]] for r in range(4)]
def muli(R, i): return [R[r] if r != i[3] else R[i[1]] * i[2] for r in range(4)]
def banr(R, i): return [R[r] if r != i[3] else R[i[1]] & R[i[2]] for r in range(4)]
def bani(R, i): return [R[r] if r != i[3] else R[i[1]] & i[2] for r in range(4)]
def borr(R, i): return [R[r] if r != i[3] else R[i[1]] | R[i[2]] for r in range(4)]
def bori(R, i): return [R[r] if r != i[3] else R[i[1]] | i[2] for r in range(4)]
def setr(R, i): return [R[r] if r != i[3] else R[i[1]] for r in range(4)]
def seti(R, i): return [R[r] if r != i[3] else i[1] for r in range(4)]
def gtir(R, i): return [R[r] if r != i[3] else 1 if i[1] > R[i[2]] else 0 for r in range(4)]
def gtri(R, i): return [R[r] if r != i[3] else 1 if R[i[1]] > i[2] else 0 for r in range(4)]
def gtrr(R, i): return [R[r] if r != i[3] else 1 if R[i[1]] > R[i[2]] else 0 for r in range(4)]
def eqir(R, i): return [R[r] if r != i[3] else 1 if i[1] == R[i[2]] else 0 for r in range(4)]
def eqri(R, i): return [R[r] if r != i[3] else 1 if R[i[1]] == i[2] else 0 for r in range(4)]
def eqrr(R, i): return [R[r] if r != i[3] else 1 if R[i[1]] == R[i[2]] else 0 for r in range(4)]
  
d = {}
opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

# start off each number (0 - 15) as being any possible opcode.
for o in range(16): d[o] = opcodes.copy()

ans = 0

# loop through the data and count many opcodes work for each sample.
# at the same time remove opcodes that didn't work from the corresponding number's dictionary values.
for n in nums:
  c = 0
  skip = False
  for o in opcodes:
    if o(n[0], n[1]) == n[2]:
      c += 1
    elif o in d[n[1][0]]:
      d[n[1][0]].remove(o)
    if c > 2 and not skip:
      ans += 1
      skip = True
      
print(ans)

i = 0
done = False

found = {}

# continuously loop through the dictionary until a key with only one value found.
# add that pair to the 'found' dictionary and remove the value from all other opcodes.
while not done:
  for k in range(16):
    if k not in d.keys(): continue
    if len(d[k]) == 1:
      found[k] = d[k][0]
      del d[k]
      for i in d.keys():
        if found[k] in d[i]:
          d[i].remove(found[k])
    done = True
  for v in d.values():
    if len(v) > 1:
      done = False

print(sorted([(k, found[k].__name__) for k in found.keys()]))


# ---------------------- PART 2 ------------------------

data2 = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2016/day16_2.txt').read().decode().split('\n')
nums2 = [ast.literal_eval(i.replace(' ', ',')) for i in data2[:-1]]

R = [0,0,0,0]

for n in nums2:
  R = found[n[0]](R, n)
  
print(R[0])
