with open("../input.txt", "r") as fp:
  data = [list(line.strip()) for line in fp]
  max_y = len(data)
  max_x = len(data[0])

def inRange(y, x):
  return 0 <= y < max_y and 0 <= x < max_x

def get_line_points(y2, x2, y1, x1):
  dy = y2 - y1
  dx = x2 - x1

  points = []

  ny, nx = (y1+dy, x1+dx)
  while inRange(ny, nx):
    points.append((ny,nx))
    ny, nx = (ny+dy, nx+dx)

  ny, nx = (y2-dy, x2-dx)
  while inRange(ny, nx):
    points.append((ny,nx))
    ny, nx = (ny-dy, nx-dx)

  return points

nodes = {}
for y in range(0, max_y):
  for x in range(0, max_x):
    ant = data[y][x]
    if ant != '.':
      if ant not in nodes:
        nodes[ant] = []
      nodes[ant].append((y,x))

antinodes = []
# Determine antinodes
for type, ants in nodes.items():
  while ants:
    ty, tx = ants.pop(0)
    for ay, ax in ants:
      antinodes.extend(get_line_points(ty, tx, ay, ax))

print(len(set(antinodes)))
