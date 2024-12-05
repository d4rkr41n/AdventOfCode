with open("../input.txt", "r") as fp:
  data = fp.read().strip().split('\n\n')

# Build rule structure
rules = {}
for line in data[0].split('\n'):
  key, value = map(int, line.split('|'))
  if key not in rules:
    rules[key] = []
  rules[key].append(value)

def checkNums(pages, a, b):
  if b not in pages:
    return True
  return pages.index(a) < pages.index(b)

# Count middle of page list for valid prints
count = 0
for line in data[1].split('\n'):
  pages = list(map(int, line.split(',')))
  valid = True
  i = 0
  while i < len(pages):
    num = pages[i]
    for rule in rules.get(num, []):
      if not checkNums(pages, num, rule):
        valid = False
        a = pages.index(num)
        b = pages.index(rule)
        pages[a], pages[b] = pages[b], pages[a]
        i = -1
        break
    i += 1

  if not valid:
    count += pages[len(pages)//2]

print(count)