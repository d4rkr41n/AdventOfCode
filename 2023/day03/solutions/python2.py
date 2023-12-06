with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def getReplaceNumber(y,x):
  if not inputs[y][x].isdigit() or inputs[y][x] == ".":
    return (0,1)
  num = [inputs[y][x]]
  xSave = x
  # Left
  x-=1
  while x >= 0 and inputs[y][x].isdigit():
    num.insert(0,inputs[y][x])
    tmp = list(inputs[y])
    tmp[x] = '.'
    inputs[y] = ''.join(tmp)
    x-=1
  # Right
  x = xSave + 1
  while x < len(inputs[y]) and inputs[y][x].isdigit():
    num += inputs[y][x]
    tmp = list(inputs[y])
    tmp[x] = '.'
    inputs[y] = ''.join(tmp)
    x+=1
  return (1,int(''.join(num)))

def findNumbers(y, x):
  if inputs[y][x] != "*":
    return 0

  product = 1
  cnt = 0

  # N
  if y-1>=0:
    tmp = getReplaceNumber(y-1, x)
    cnt += tmp[0]
    product *= tmp[-1]
    # NW
    if x-1>=0:
      tmp = getReplaceNumber(y-1, x-1)
      cnt += tmp[0]
      product *= tmp[-1]
    # NE
    if x+1<len(inputs[y]):
      tmp = getReplaceNumber(y-1, x+1)
      cnt += tmp[0]
      product *= tmp[-1]

    # S
    if y+1<len(inputs):
      tmp = getReplaceNumber(y+1, x)
      cnt += tmp[0]
      product *= tmp[-1]
      # SW
      if x-1>=0:
        tmp = getReplaceNumber(y+1, x-1)
        cnt += tmp[0]
        product *= tmp[-1]
      # SE
      if x+1<len(inputs[y]):
        tmp = getReplaceNumber(y+1, x+1)
        cnt += tmp[0]
        product *= tmp[-1]

  # W
  if x-1>=0:
    tmp = getReplaceNumber(y, x-1)
    cnt += tmp[0]
    product *= tmp[-1]
  # E
  if x+1<len(inputs[y]):
    tmp = getReplaceNumber(y, x+1)
    cnt += tmp[0]
    product *= tmp[-1]

  return product if (product != 1 and cnt > 1) else 0

finalSum = 0
for y in range(0,len(inputs)):
  for x in range(0,len(inputs[y])):
    finalSum += findNumbers(y,x)

print(finalSum)