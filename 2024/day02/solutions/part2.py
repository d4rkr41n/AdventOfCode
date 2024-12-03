with open("../input.txt", "r") as fp:
  inputs = [list(map(int, line.rstrip().split())) for line in fp]

def is_safe(line, rec=True):
  increase = 0
  decrease = 0

  for i, a in enumerate(line[:-1]):
    b = line[i+1]

    # Check for difference of 1-3
    if abs(a-b) > 3 or abs(a-b) < 1:
      if rec:
        case_0 = line[:]
        case_0.pop(0)
        case_1 = line[:]
        case_1.pop(i)
        case_2 = line[:]
        case_2.pop(i+1)
        if is_safe(case_0, False) or is_safe(case_1, False) or is_safe(case_2, False):
          return True

      return False

    # Watch for increase/decrease
    if a < b:
      increase += 1
    else:
      decrease += 1

    if increase != 0 and decrease != 0:
      if rec:
        case_0 = line[:]
        case_0.pop(0)
        case_1 = line[:]
        case_1.pop(i)
        case_2 = line[:]
        case_2.pop(i+1)
        if is_safe(case_0, False) or is_safe(case_1, False) or is_safe(case_2, False):
          return True

      return False

  return True

safe = 0
for line in inputs:
  if is_safe(line):
    safe += 1

print(safe)