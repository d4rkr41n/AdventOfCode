from PIL import ImageDraw
from PIL import Image

with open("../input.txt", "r") as fp:
  map = fp.read().strip().split("\n")

out = Image.new("RGB", (len(map[0]), len(map)), (255, 255, 255))

directions = {
  '|': [(1,0),(-1,0)],
  '-': [(0,1),(0,-1)],
  'J': [(-1,0),(0,-1)],
  'L': [(-1,0),(0,1)],
  'F': [(1,0),(0,1)],
  '7': [(1,0),(0,-1)]
}
graph = {}

# Find S
py = 0
px = 0
for y,row in enumerate(map):
  if 'S' in row:
    py = y
    px = map[y].index('S')
graph[f"{py}|{px}"] = 0

p = [py, px]
start = p

# Find all the paths starting at S
paths = []
for i,dir in enumerate([(-1,0),(1,0),(0,1),(0,-1)]):
  v,h = dir
  # Get all transforms for symbol at loc
  transforms = directions.get(map[py+v][px+h])
  if not transforms:
    continue

  for t,transform in enumerate(transforms):
    tv,th = transform
    # If the path gets us back to start then its valid
    if(py+v+(tv) == py and px+h+(th) == px):
      paths.append([py+v,px+h])

# Determine what symbol S should be
possibles = []
for y,x in paths:
  gy = (py-y)*-1
  gx = (px-x)*-1
  possibles.append((gy,gx))
for d in directions:
  if possibles[0] in directions[d] and possibles[1] in directions[d]:
    tmp = list(map[py])
    tmp[px] = d
    map[py] = ''.join(tmp)

# Loop over possible paths from S
for path in paths:
  p = path
  dist = 1
  posD = graph.get(f"{p[0]}|{p[1]}")
  while posD is None or posD > dist:
    py,px = p

    graph[f"{py}|{px}"] = dist

    out.putpixel((px, py), (50, 50, 50))

    # JIC cases :)
    if py > len(map)-1 or py < 0:
      break
    if px > len(map[py])-1 or px < 0:
      break

    sym = map[py][px]
    transforms = directions.get(sym)

    for transform in transforms:
      tv,th = transform
      posD = graph.get(f"{tv+py}|{th+px}")

      if posD is None or posD > dist+1:
        p = [tv+py,th+px]
        break
    dist += 1

# raytrace the entire polygon
inPixels = []
for y in range(len(map)):
  inside = 0
  prevCorner = ""
  for x in range(len(map[y])):
    sym = graph.get(f"{y}|{x}")

    if sym is not None:
      if map[y][x] in "|JL":
        inside += 1
    elif sym is None and inside % 2 == 1:
      inPixels.append((y,x))

# Color da map
for y,x in inPixels:
  out.putpixel((x,y), (100, 0, 255))

total = len(inPixels)
print(total)

out.save("./part2.png")
