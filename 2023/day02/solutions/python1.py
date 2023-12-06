with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

limit = {
  "red": 12,
  "green": 13,
  "blue": 14
}

sum = 0
for line in inputs:
  id = int(line.split(':')[0].split(' ')[-1])
  game = line.split(':')[-1]
  rounds = game.split(';')

  impossible = False
  for round in rounds:
    blocks = round.split(",")
    for block in blocks:
      num = int(block.strip().split(' ')[0])
      color = block.strip().split(' ')[-1]
      if num > limit.get(color):
        impossible = True
        break

  if not impossible:
    sum += id

print(sum)