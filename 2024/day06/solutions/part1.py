with open("../input.txt", "r") as fp:
  inputs = [list(line.rstrip()) for line in fp]

syms = ['^','>','v','<']
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = 0

guard_y = -1
guard_x = -1
for y,line in enumerate(inputs):
  for x,char in enumerate(line):
    if char not in syms:
      continue
    guard_y = y
    guard_x = x
    cur_dir = syms.index(inputs[guard_y][guard_x])
    break
  if guard_x != -1:
    break

def right(index):
  return (index + 1) % len(dir)

steps = 0
# Walk the guard through the maze
while (guard_x >= 0 and guard_x < len(inputs[0])) and (guard_y >= 0 and guard_y < len(inputs)):
  char = inputs[guard_y][guard_x]

  if char == '#':
    # Backtrack and turn
    my, mx = dir[(cur_dir+2)%4]
    guard_y += my
    guard_x += mx
    cur_dir = right(cur_dir)
  else:
    inputs[guard_y][guard_x] = 'X'

  my,mx = dir[cur_dir]
  guard_y += my
  guard_x += mx

count = 0
for row in inputs:
  count += row.count('X')

print(count)
