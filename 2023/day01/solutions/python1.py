with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

sum = 0
for line in inputs:

  digits = []
  # Forwards
  for i, char in enumerate(line):
    if(ord(char) > 47 and ord(char) < 58):
      digits += char
      break

  # Backwards
  for i, char in enumerate(reversed(line)):
    if(ord(char) > 47 and ord(char) < 58):
      digits += char
      break

  sum += int(''.join(digits))

print(sum)