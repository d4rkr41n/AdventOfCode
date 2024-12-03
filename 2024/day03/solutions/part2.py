import re

with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def mul(a,b):
  return a*b

mul_reg = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)")

sum = 0
do = True
for line in inputs:
  result = re.findall(mul_reg, line)
  for group in result:
    if "don't" in group:
      do = False
    elif "do" in group:
      do = True
    elif "mul" in group and do:
      sum += eval(group)

print(sum)