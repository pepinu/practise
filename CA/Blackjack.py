result = []
spec = ['T', 'J', 'Q', 'K']
times = input()
for i in range(times):
  points = 0
  cards = raw_input().split()
  i = 0
  while points < 21 and i != len(cards):
    if cards[i] in spec:
      points += 10
    elif points <= 10 and cards[i] == 'A':
      points += 11
    elif points > 10 and cards[i] == 'A':
      points += 1
    else:
      points += int(cards[i]) 
    i += 1
  if points > 21:
    result.append("Bust")
  else:
    result.append(points)
print ' '.join(map(str, result))
    
  
