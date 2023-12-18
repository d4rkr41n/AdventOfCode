with open("../input.txt", "r") as fp:
  inputs = fp.read().strip().split("\n")

expand = 1000000-1
xDomains = []

def _dist(x1,y1,x2,y2):
  x3 = x2-x1
  y3 = y2-y1

  warp = 0
  xr = range(min(x1,x2),max(x1,x2)+1)
  yr = range(min(y1,y2),max(y1,y2)+1)
  for x,y in xDomains:
    if x in xr:
      warp += expand
    if y in yr:
      warp += expand

  return abs(x3)+abs(y3)+warp

# Expand the Universe Height
length = len(inputs)
i = 0
while i < length:
  if len(inputs[i].replace('.','')) == 0:
    xDomains.append((-1,i))
  i+=1

# Expand the Universe Width
length = len(inputs[0])
i = 0
while i < length:
  if len(''.join([inputs[s][i] for s in range(len(inputs))]).replace('.','')) == 0:
    xDomains.append((i,-1))
  i+=1

# Extract the points
points = []
for y,row in enumerate(inputs):
  index = -1
  while True:
    try:
      index = row.index("#", index + 1)
    except ValueError:
      break
    points.append((y,index))

total = 0
for p,point in enumerate(points):
  y1,x1 = point
  for t,test in enumerate(points[p+1:]):
    y2,x2 = test
    if point == test:
      continue
    res = _dist(x1,y1,x2,y2)
    total += res

print(total)
