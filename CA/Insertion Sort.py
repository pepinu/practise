def insertionsrt(x, y):
  for i in range(1, len(x)):
    temp = i
    pss = 0
    while temp > 0 and x[temp-1] > x[temp]:
      x[temp], x[temp-1] = x[temp-1], x[temp]
      pss += 1
      temp -= 1
    y.append(pss)
  return x

times = input()
result = []
sort = [] 
arr = raw_input().split()
arr = map(int, arr)
insertionsrt(arr, result)
print ' '.join(map(str, result))
      
