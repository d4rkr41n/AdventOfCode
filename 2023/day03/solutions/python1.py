with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def getReplaceNumber(y,x):
    if not inputs[y][x].isdigit() or inputs[y][x] == ".":
        return 0
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
    return int(''.join(num))

def findNumbers(y, x):
    if inputs[y][x].isdigit() or inputs[y][x] == ".":
        return 0

    sum = 0

    # N 
    if y-1>=0:
        sum += getReplaceNumber(y-1, x)
        # NW
        if x-1>=0:
            sum += getReplaceNumber(y-1, x-1)
        # NE 
        if x+1<len(inputs[y]):
            sum += getReplaceNumber(y-1, x+1)
        
    # S
    if y+1<len(inputs):
        sum += getReplaceNumber(y+1, x)
        # SW
        if x-1>=0:
            sum += getReplaceNumber(y+1, x-1)
        # SE 
        if x+1<len(inputs[y]):
            sum += getReplaceNumber(y+1, x+1)
        
    # W
    if x-1>=0:
        sum += getReplaceNumber(y, x-1)
    # E 
    if x+1<len(inputs[y]):
        sum += getReplaceNumber(y, x+1)

    return sum

finalSum = 0
for y in range(0,len(inputs)):
    for x in range(0,len(inputs[y])):
        finalSum += findNumbers(y,x)

print(finalSum)