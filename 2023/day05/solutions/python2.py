with open("../input.txt", "r") as fp:
  seeds, *blocks = fp.read().strip().split("\n\n")
seeds = [int(x) for x in seeds.split()[1:]]

def get_ranges(src_ranges, mapping):
  result = []
  for a, b in src_ranges:
    usedRanges = []
    for d, s, r in mapping:
      x, y = s, s+r-1
      # Short circuit if we aren't in range
      if b < x or y < a:
        continue

      big = max(a, x)
      smol = min(b, y)
      usedRanges.append((big, smol))
      result.append((big-s+d, smol-s+d))

    # If we don't find a range then make a new one
    if not usedRanges:
      result.append((a, b))
      continue

    usedRanges.sort()
    # Fill the beginning range out
    if usedRanges[0][0] > a:
      result.append((a, usedRanges[0][0]-1))

    # fill the end
    if usedRanges[-1][1] < b:
      result.append((usedRanges[-1][1]+1, b))
    for i in range(len(usedRanges)-1):
      x1, y1 = usedRanges[i]
      x2, y2 = usedRanges[i+1]
      if x2 > y1+1:
        result.append((y1+1, x2-1))
  return result

maps = []
for block in blocks:
  lines = block.split('\n')[1:]
  map_ = []
  for line in lines:
    map_.append( tuple(map(int, line.split())) )
  maps.append(map_)

# Make a lookup table (bottom,top)
seedRanges = []
for i in range(0, len(seeds), 2):
  seedRanges.append((seeds[i], seeds[i]+seeds[i+1]-1))

for mapping in maps:
  seedRanges = get_ranges(seedRanges, mapping)

print(min(seedRanges)[0])