with open("../input.txt", "r") as fp:
  instructions, *maze = fp.read().strip().split("\n\n")
maze = [x.split(' = ') for x in ''.join(maze).split('\n')]

map = {}
for i in maze:
  map[i[0]] = (i[1][1:-1].split(', '))

camel = 'AAA'
steps = 0
while camel != 'ZZZ':
  for i in instructions:
    dir = 0
    if i == 'R':
      dir = -1

    camel = map[camel][dir]
    steps += 1
    if camel == 'ZZZ':
      break

print(steps)