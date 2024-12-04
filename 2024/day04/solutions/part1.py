with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

nextChar = {
  'X': 'M',
  'M': 'A',
  'A': 'S'
}

def checkWord(inputs, char, pos, dir):
  # What to check, () pos, () direction traveling
  py, px = pos
  dy, dx = dir

  if inputs[py][px] == char:
    if char == 'S':
      return True

    py += dy
    px += dx
    if px < 0 or px >= len(inputs[0]):
      return False
    elif py < 0 or py >= len(inputs):
      return False

    return checkWord(inputs, nextChar.get(char), (py,px), (dy,dx))

  return False

count = 0
for y,line in enumerate(inputs):
  for x,char in enumerate(line):
    for dy,dx in [(0,-1),(0,1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]:
      if checkWord(inputs,'X',(x,y),(dy,dx)):
        count += 1

print(count)