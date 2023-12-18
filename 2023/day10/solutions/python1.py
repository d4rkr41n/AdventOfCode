from PIL import ImageDraw
from PIL import Image

with open("../input.txt", "r") as fp:
  map = fp.read().strip().split("\n")

out = Image.new("RGB", (len(map)*2, len(map[0])*2), (255, 255, 255))

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

  for transform in transforms:
    tv,th = transform
    # If the path gets us back to start then its valid
    if(py+v+(tv) == py and px+h+(th) == px):
      paths.append([py+v,px+h])

# Loop over possible paths from S
for path in paths:
  p = path
  dist = 1
  posD = graph.get(f"{p[0]}|{p[1]}")
  while posD is None or posD > dist:
    py,px = p
    graph[f"{py}|{px}"] = dist

    out.putpixel((px*2, py*2), (255, 0, 0))

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

      # If we just came from there then ignore
      if posD is None or posD > dist+1:
        p = [tv+py,th+px]
        # fill pixel gap
        out.putpixel(((th+px)*2-th, (tv+py)*2-tv), (255, 0, 0))
        break
    dist += 1

maxLoc = [int(i) for i in max(graph, key=graph.get).split('|')]

out.putpixel((start[0]*2, start[1]*2), (0, 255, 0))
out.putpixel((maxLoc[0]*2, maxLoc[1]*2), (0, 0, 255))
out.save("./part1.png")

print(graph['|'.join([str(i) for i in maxLoc])])
