with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def checkWord(inputs, pos):
  py, px = pos

  if py-1 < 0 or py+1 >= len(inputs):
    return 0
  if px-1 < 0 or px+1 >= len(inputs[0]):
    return 0

  TL = inputs[py-1][px-1]
  BR = inputs[py+1][px+1]
  if TL+'A'+BR != "MAS" and TL+'A'+BR != "SAM":
    return 0

  TR = inputs[py-1][px+1]
  BL = inputs[py+1][px-1]
  if TR+'A'+BL != "MAS" and TR+'A'+BL != "SAM":
    return 0

  return 1

count = 0
for y,line in enumerate(inputs):
  for x,char in enumerate(line):
    if char == 'A':
      count += checkWord(inputs,(y,x))

print(count)