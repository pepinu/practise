result = []
loops = int(raw_input())
for i in range(loops):
  winner = [0, 0]
  nums = raw_input().split()
  for c in nums:
    match = list(c)
    if match[0] != match[1]:
      if match[0] == 'P' and match[1] == 'R':
        winner[0] += 1  
      elif match[0] == 'R' and match[1] == 'S':
        winner[0] += 1 
      elif match[0] == 'S' and match[1] == 'P': 
        winner[0] += 1 
      else:
        winner[1] += 1 

  if winner[0] > winner[1]:
    result.append(1)
  else:
    result.append(2)
print ' '.join(map(str, result))


