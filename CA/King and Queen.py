result = []
times = input()
for i in range(times):
  pos = raw_input().split()
  if pos[0][0] == pos[1][0]:
    result.append('Y')
  elif pos[0][1] == pos[1][1]:
    result.append('Y')
  elif abs(ord(pos[0][1]) - ord(pos[1][1])) == abs(ord(pos[0][0]) - ord(pos[1][0])):
    result.append('Y')
  else:
    result.append('N')
  
print ' '.join(map(str, result))
    
  
