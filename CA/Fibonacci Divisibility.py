def fibo(a):
  arr = []
  res = 0
  ser = 1
  arr.append(res) 
  if a == 0:
    return arr
  arr.append(ser)
  if a == 1:
    return arr
  if a > 1:
    for i in range(1,a):
      ans = res + ser
      res = ser
      ser = ans
      arr.append(ser)
  return arr

result = []
fibbo = fibo(10000)
loops = input()
divisors = raw_input().split()
divisors = map(int, divisors)
for i in divisors:
  a = 1
  while fibbo[a] % i != 0 :
    a += 1
  result.append(a)
print ' '.join(map(str,result))

