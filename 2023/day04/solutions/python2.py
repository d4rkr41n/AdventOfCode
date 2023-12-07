import json
with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

def scoreCard(lines, wins):
  winners, nums = lines[0].split(':')[-1].split('|')
  winners = list(filter(None, winners.strip().split(' ')))
  nums = nums.replace("  "," ")+" "

  cnt = 0
  for winner in winners:
    cnt += nums.count(" "+winner+" ")

  score = 1
  if wins > 0:
    score += scoreCard(lines[1:], wins-1)
  if cnt > 0:
    score += scoreCard(lines[1:], cnt-1)
  return score

sum = 0
for i,line in enumerate(inputs):
  sum += scoreCard(inputs[i:], -1)
print(sum)
