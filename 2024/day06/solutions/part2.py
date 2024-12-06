with open("../input.txt", "r") as fp:
  inputs = [list(line.rstrip()) for line in fp]

def turnRight(index):
  return (index + 1) % len(directions)

def getStart(inputs):
  syms = ['^','>','v','<']
  for y, row in enumerate(inputs):
    for x, char in enumerate(inputs[y]):
      if char in syms:
        return y,x,syms.index(char)

def getPathTouches(inputs, gy, gx, dir):
  touches = []
  while gy < len(inputs) and gy >= 0 and gx < len(inputs[0]) and gx >= 0:
    if inputs[gy][gx] == '#':
      # back up and turn
      gy += directions[(dir+2)%4][0]
      gx += directions[(dir+2)%4][1]
      dir = turnRight(dir)

    touches.append((gy,gx))
    gy += directions[dir][0]
    gx += directions[dir][1]
  return touches

def testForLoop(inputs, gy, gx, oy, ox, dir):
  hashmap = {}
  while gy < len(inputs) and gy >= 0 and gx < len(inputs[0]) and gx >= 0:
    if hashmap.get(f"{gy},{gx},{dir}", False):
      return 1

    if inputs[gy][gx] == '#' or (gy == oy and gx == ox):
      # back up and turn
      gy += directions[(dir+2)%4][0]
      gx += directions[(dir+2)%4][1]
      dir = turnRight(dir)

    hashmap[f"{gy},{gx},{dir}"] = True
    gy += directions[dir][0]
    gx += directions[dir][1]
  return 0

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
gy,gx,dir = getStart(inputs)

# build a list of spaces the guard touches (reduce time complexity)
touches = getPathTouches(inputs, gy, gx, dir)

# Test Blockers in those spots (except the guard spot)
count = 0
for oy, ox in set(touches[1:]):
  count += testForLoop(inputs, gy, gx, oy, ox, dir)

print(count)
