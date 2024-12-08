with open("../input.txt", "r") as fp:
  inputs = [
    [int(result), list(map(int, nums.split()))]
    for line in fp
    if (result := line.split(':')[0]) and (nums := line.split(':')[1].strip())
  ]

def checkOps(num, res, ops, index=0):
    if index == len(ops):
        return res == num

    addition_result = checkOps(num, res + ops[index], ops, index + 1)
    if addition_result:
        return True

    multiplication_result = checkOps(num, res * ops[index], ops, index + 1)
    if multiplication_result:
        return True

    concatination_result = checkOps(num, int(f"{res}{ops[index]}"), ops, index + 1)
    return concatination_result

total_cal = 0
for input in inputs:
    num = input[0]
    ops = input[1]
    total_cal += num if checkOps(num, 0, ops) else 0

print(total_cal)
