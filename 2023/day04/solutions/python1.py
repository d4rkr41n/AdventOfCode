with open("../input.txt", "r") as fp:
  inputs = [line.rstrip() for line in fp]

sum = 0
for line in inputs:
  id = line.split(':')[0]
  winners, nums = line.split(':')[-1].split('|')
  winners = list(filter(None, winners.strip().split(' ')))
  nums = nums.replace("  "," ")+" "

  cnt = 0
  for winner in winners:
    cnt += nums.count(" "+winner+" ")
  sum += int(pow(2, cnt-1))

print(sum)