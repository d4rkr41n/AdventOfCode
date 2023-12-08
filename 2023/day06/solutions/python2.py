import math

with open("../input.txt", "r") as fp:
  input = fp.read().strip().split("\n")

race = (
  int(''.join(input[0].split()[1:])),
  int(''.join(input[-1].split()[1:])),
)

time = race[0]
record = race[-1]+1

min = math.ceil((time - math.sqrt(time*time - 4 * record))/2)
max = math.floor((time + math.sqrt(time*time - 4 * record))/2)
product = (max-min+1)

print(product)