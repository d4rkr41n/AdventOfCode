with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

numberMap = {}
arr1 = []
arr2 = []

for line in inputs:
  tmp = list(filter(None, line.strip().split(' ')))
  arr1.append(int(tmp[0]))
  arr2.append(int(tmp[1]))

# Map the number counts
for b in arr2:
  if b not in numberMap:
    numberMap[b] = 1
  else:
    numberMap[b] += 1

# Calculate similarity score
sim = 0
for a in arr1:
  sim += a * numberMap.get(a, 0)

print(sim)