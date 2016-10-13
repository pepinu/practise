def fibo(a):
  res = 0
  if a == 0:
    res = 0
  elif a == 1:
    res = 1
  else:
    res = fibo(a-1) + fibo(a-2)
  return res

result = []
loops = int(raw_input())
for i in range(loops):
  a = 0
  num = long(raw_input())
  while fibo(a) != num:
     a += 1
  result.append(a)  
print ' '.join(map(str,result))

