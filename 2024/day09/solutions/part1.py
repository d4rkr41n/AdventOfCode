with open("../input.txt", "r") as fp:
  input = []
  id = 0
  for i, char in enumerate(fp.read().strip()):
    item = int(char)
    sym = id if i % 2 == 0 else -1
    id += 1 if i % 2 == 0 else 0
    input.extend([sym] * item)

# Do the swapping
inc, dec = 0, len(input)-1
while inc < dec:
  # find hole and last number
  while inc < dec and input[inc] >= 0:
    inc += 1
  while inc < dec and input[dec] == -1:
    dec -= 1

  if inc < dec:
    input[inc], input[dec] = input[dec], input[inc]
    inc += 1
    dec -= 1

# now calc the checksum
checksum = 0
for i, num in enumerate(input):
  if num >= 0:
    checksum += i * num

print(checksum)
