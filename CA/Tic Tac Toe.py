times = input()
win= [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7] ]
result = []
for i in range(times):
  won = 0
  move = 0
  X = []
  O = []
  moves = raw_input().split()
  moves = map(int,moves)
  for j in range(len(moves)):
    if j % 2 == 0:
      X.append(moves[j])

    else:
      O.append(moves[j])
    move += 1

    if won == 1:
      break
    for b in win:
      for a in range(1):
        if b[a] in X and b[a+1] in X and b[a+2] in X:
          won = 1
          break
        if b[a] in O and b[a+1] in O and b[a+2] in O:
          won = 1
          break
      if won == 1:
        result.append(move)
        break
        

  if won == 0:
    result.append(0)
  
 
  

#  result.append(x)
print O, X 
print ' '.join(map(str, result))
      
