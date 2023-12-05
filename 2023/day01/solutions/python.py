with open("../input.txt", "r") as fp:
  inputs = fp.readlines()

numbers = ["one","two","three","four","five","six","seven","eight","nine"]

sum = 0
for line in inputs:

  digits = []
  # Forwards
  for i, char in enumerate(line):
    if(ord(char) > 47 and ord(char) < 58):
      digits += char
      break

    for j, num in enumerate(numbers):
      if(line[i:].startswith(num)):
        digits += str(j+1)
        break
    if(len(digits) > 0):
      break

  # Backwards
  for i, char in enumerate(reversed(line)):
    if(ord(char) > 47 and ord(char) < 58):
      digits += char
      break

    for j, num in enumerate(numbers):
      if((line[::-1])[i:].startswith(num[::-1])):
        digits += str(j+1)
        break
    if(len(digits) > 1):
      break

  sum += int(''.join(digits))

print(sum)