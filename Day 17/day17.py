from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np
import re

data = urlopen('https://raw.githubusercontent.com/MarynaLongnickel/AdventOfCode2018/master/Day%2017/day17.txt').read().decode().split('\n')[:-1]

coor = []

# parse data and collect the coordinates of clay
for d in data:
    nums = [int(i) for i in re.findall(r'\d+', d)]
    if d[0] == 'x':
        coor.extend([(nums[0], i) for i in range(nums[1], nums[2] + 1)])
    else:
        coor.extend([(i, nums[0]) for i in range(nums[1], nums[2] + 1)])

x, y = zip(*coor)
minx, maxx = min(x), max(x)
miny, maxy = min(y), max(y)

# initialize the scan and fill it in wherever there is clay
scan = [['.' for i in range(maxx - minx + 1)] for j in range(maxy + 1)]

for c in coor: scan[c[1]][c[0] - minx] = '#'

# starting point
x, y = 500 - minx + 1, 0

# number of water cells that are pooled in the clay or overflowing
pool = fall = 0

# fill in the water cells
def flow(scan, x, y, d):
    if scan[y][x] == '.':
        scan[y][x] = '|'
    if y == len(scan) - 1:
        return
    if scan[y][x] == '#':
        return x
    if scan[y + 1][x] == '.':
        flow(scan, x, y + 1, 0)

    if scan[y + 1][x] in '~#':
        if d:
            return flow(scan, x + d, y, d)
        else:
            scanL = flow(scan, x - 1, y, -1)
            scanR = flow(scan, x + 1, y, 1)
            if scan[y][scanL] == '#' and scan[y][scanR] == '#':
                for c in range(scanL + 1, scanR):
                    scan[y][c] = '~'
    else:
        return x


flow(scan, x, y, 0)

# count pooled and falling water cells
for y in range(len(scan)):
    for x in range(len(scan[0])):
        if scan[y][x] == '|':
            fall += 1
        elif scan[y][x] == '~':
            pool += 1

print(pool + fall - 1, pool)
