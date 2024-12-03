import re

with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def mul(a,b):
  return a*b

mul_reg = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")

sum = 0
for line in inputs:
  result = re.findall(mul_reg, line)
  for group in result:
    sum += eval(group)

print(sum)