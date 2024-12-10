with open("../input.txt", "r") as fp:
  inputs = [list(map(int, line.strip())) for line in fp]

def countPaths(hy, hx):
  finished = []
  paths = [(hy,hx)]
  while paths:
    hy, hx = paths.pop(0)
    for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ny, nx = hy + y, hx + x

      if 0 <= ny < len(inputs) and 0 <= nx < len(inputs[0]) and inputs[ny][nx] == inputs[hy][hx] + 1:
        if inputs[ny][nx] == 9:
          finished.append((ny,nx))
        else:
          paths.append((ny,nx))

  return len(set(finished))

paths = 0
for y in range(0, len(inputs)):
  for x in range(0, len(inputs[y])):
    if inputs[y][x] == 0:
      paths += countPaths(y, x)

print(paths)
