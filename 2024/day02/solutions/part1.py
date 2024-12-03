with open("../input.txt", "r") as fp:
  inputs = [list(map(int, line.rstrip().split())) for line in fp]

safe = 0

for line in inputs:
  increase = 0
  decrease = 0
  unsafe = False
  for i, a in enumerate(line[:-1]):
    b = line[i+1]

    # Check for difference of 1-3
    if abs(a-b) > 3 or abs(a-b) < 1:
      unsafe = True
      break

    # Watch for increase/decrease
    if a < b:
      increase += 1
    else:
      decrease += 1

    if increase != 0 and decrease != 0:
      unsafe = True
      break

  if not unsafe:
    safe += 1

print(safe)