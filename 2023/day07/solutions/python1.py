with open("../input.txt", "r") as fp:
  input = fp.read().strip().split("\n")

ranks = [[],[],[],[],[],[],[]]
strengths = "AKQJT98765432"[::-1]

def insertRank(hand, t):
  pos = -1
  if not ranks[t]:
    ranks[t].insert(pos, hand)
    return

  for p, player in enumerate(ranks[t]):
    player = player[0]

    for c, card in enumerate(hand[0]):
      pCard = strengths.find(card)
      rCard = strengths.find(player[c])

      if pCard < rCard:
        ranks[t].insert(p, hand)
        return
      elif pCard > rCard and p+1 == len(ranks[t]):
        ranks[t].insert(p+1, hand)
        return
      elif pCard > rCard:
        break

for player in input:
  cards = player.split()[0]
  bet = int(player.split()[-1])

  c = set([cards.count(x) for x in cards])
  counts = len(''.join(set(cards)))

  if counts == 5:
    # High Card
    insertRank((cards,bet), 6)
  elif counts == 4:
    # One Pair
    insertRank((cards,bet), 5)
  elif counts == 3:
    # Two Pair: 22334
    c = set([cards.count(x) for x in cards])
    if 2 in c:
      insertRank((cards,bet), 4)
    else:
      # Three of a kind: 22234
     insertRank((cards,bet), 3)
  elif counts == 2:
    # Full House: 23332
    c = set([cards.count(x) for x in cards])
    if 2 in c:
      insertRank((cards,bet), 2)
    else:
      # Four of a kind: 22223
      insertRank((cards,bet), 1)
  elif counts == 1:
    # Five of a kind
    insertRank((cards,bet), 0)

sum = 0
i = 1
for r in reversed(ranks):
  for cards, bet in r:
    sum += (bet*i)
    i += 1

print(sum)
