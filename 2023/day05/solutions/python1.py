with open("../input.txt", "r") as fp:
  seeds, *blocks = fp.read().split("\n\n")
seeds = list(map(int, seeds.split(':')[1].split()))

maps = []
for block in blocks:
  line = block.split('\n')[1:]
  mapInstance = []
  for i,item in enumerate(line):
    items = item.split(' ')
    mapInstance.append( list(map(int, items)) )
  maps.append(mapInstance)

def recMaps(value, mapI):
  if mapI+1 > len(maps):
    return value

  for r in maps[mapI]:
    if value >= r[1] and value < r[1]+r[2]:
      value = value-r[1]+r[0]
      break

  return recMaps(value, mapI+1)

locations = []
for seed in seeds:
  locations.append( recMaps(seed,0) )
print(min(locations))