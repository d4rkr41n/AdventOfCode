with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

sum = 0
for line in inputs:
  id = int(line.split(':')[0].split(' ')[-1])
  game = line.split(':')[-1]
  rounds = game.split(';')

  rgb = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for round in rounds:
    blocks = round.split(",")
    for block in blocks:
      num = int(block.strip().split(' ')[0])
      color = block.strip().split(' ')[-1]

      if num > rgb.get(color):
        rgb[color] = num;

  sum += (rgb["red"] * rgb["green"] * rgb["blue"])

print(sum)