with open("../input.txt", "r") as fp:
  inputs = fp.read().strip().split("\n")
for i, inp in enumerate(inputs):
  inputs[i] = list(map(int,inputs[i].split()))

sum = 0
for seq in inputs:
  seq = seq[::-1]
  rows = []
  while len(seq) > 0 and set(seq) != {0}:
    rows.append(seq)
    tmp = seq
    seq = []
    for i in range(len(tmp) - 1):
      seq.append(tmp[i + 1] - tmp[i])

  for r in rows:
    sum += r[-1]

print(sum)