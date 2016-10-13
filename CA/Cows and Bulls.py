result = []
loops = raw_input().split()
check = list(loops[0])
_try = raw_input().split()
for a in _try:
  find = list(a)
  guess = [0,0]
  for x in range(len(a)):
    if a[x] in check and a[x] != check[x]:
      guess[1] += 1
    elif a[x] in check and a[x] == check[x]:
      guess[0] += 1
  result.append('-'.join(map(str,guess)))
print ' '.join(map(str, result))


