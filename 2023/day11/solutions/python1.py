with open("../input.txt", "r") as fp:
  inputs = fp.read().strip().split("\n")

def _dist(x1,y1,x2,y2):
  x = x2-x1
  y = y2-y1
  return abs(x)+abs(y)

# Expand the Universe Height
length = len(inputs)
i = 0
while i < length:
  if len(inputs[i].replace('.','')) == 0:
    inputs.insert(i,inputs[i])
    length += 1
    i += 1
  i+=1

# Expand the Universe Width
length = len(inputs[0])
i = 0
while i < length:
  if len(''.join([inputs[s][i] for s in range(len(inputs))]).replace('.','')) == 0:
    for s in range(len(inputs)):
      new = list(inputs[s])
      new.insert(i,inputs[0][i])
      inputs[s] = ''.join(new)
    length += 1
    i += 1
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
