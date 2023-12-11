from math import gcd

with open("../input.txt", "r") as fp:
  instructions, *maze = fp.read().strip().split("\n\n")
maze = [x.split(' = ') for x in ''.join(maze).split('\n')]

map = {}
for i in maze:
  map[i[0]] = (i[1][1:-1].split(', '))

camels = []
for i in map.keys():
  if i[-1] == 'A':
    camels.append(i)
intervals = []

for i, camel in enumerate(camels):
  interval = 0

  while camel[-1] != 'Z':
    for ins in instructions:
      dir = 0
      if ins == 'R':
        dir = -1
      camel = map[camel][dir]
      interval += 1

      if camel[-1] == 'Z':
        intervals.append(interval)
        break

lcm = 1
for i in intervals:
  lcm = lcm*i//gcd(lcm, i)

print(lcm)
