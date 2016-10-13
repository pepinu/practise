def fibo(a):
  res = 0
  ser = 1
  if a == 0:
    return res
  elif a == 1:
    return ser
  else:
    for i in range(a):
      ans = res + ser
      res = ser
      ser = ans
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

