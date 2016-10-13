def fly(x, y, z, r):
  t1 = []
  t2 = []
  stepx = 1
  stepy = 1
  i = 0
  j = 0
  iters = 0
  while len(t1) != 101:
    if i <= x - z and i > -1: 
      t1.append(i)
      iters += 1
    else:
      stepx *= -1
      i += stepx
    i += stepx 
  while len(t2) != 101:
    if j < y  and j > -1: 
      t2.append(j)
      iters += 1
    else:
      stepy *= -1
      j += stepy
    j += stepy

  for i in range(101):
    r.append(t1[i])
    r.append(t2[i])


result = []
sort = [] 
arr = raw_input().split()
arr = map(int, arr)
fly( arr[0], arr[1], arr[2], result)
print ' '.join(map(str, result))

      
