with open("../input.txt", "r") as fp:
  input = []
  id = 0
  for i, char in enumerate(fp.read().strip()):
    item = int(char)
    sym = id if i % 2 == 0 else -1
    id += 1 if i % 2 == 0 else 0
    input.extend([sym] * item)

inc, dec = 0, len(input)-1
while inc < dec and dec >= 0:
  # find hole and last number
  while inc < dec and input[inc] >= 0:
    inc += 1
  while inc < dec and input[dec] == -1:
    dec -= 1

  sym = input[dec]
  scnt = 0
  # count how big the file is
  while input[dec] == sym and 0 <= dec:
    scnt += 1
    dec -= 1
  dec += 1

  hcnt = 0
  # search for a spot (from the front) to fit that many
  while inc <= dec and hcnt != scnt:
    hcnt += 1
    if input[inc] != -1:
      hcnt = 0
    inc += 1
  inc -= 1

  if hcnt == scnt:
    for i in range(0, hcnt):
      input[inc-i] = sym
      input[dec+i] = -1

  # in case a hole doesnt get used :(
  inc = 0
  dec -= 1

# now calc the checksum
checksum = 0
for i, num in enumerate(input):
  if num >= 0:
    checksum += i * num

print(checksum)
