with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

arr1 = []
arr2 = []

for line in inputs:
  tmp = list(filter(None, line.strip().split(' ')))
  arr1.append(int(tmp[0]))
  arr2.append(int(tmp[1]))

arr1.sort()
arr2.sort()

sum = 0
for a, b in zip(arr1, arr2):
  sum += abs(a - b)

print(sum)