import math

with open("../input.txt", "r") as fp:
  input = fp.read().strip().split("\n")

races = list(zip(
  [int(x) for x in input[0].split()[1:]],
  [int(x) for x in input[-1].split()[1:]]
))

product = 1
for time, record in races:
  record += 1
  min = math.ceil((time - math.sqrt(time*time - 4 * record))/2)
  max = math.floor((time + math.sqrt(time*time - 4 * record))/2)

  product *= (max-min+1)
print(product)