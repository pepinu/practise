result = []
letters = raw_input().split()
letters = map(int, letters)
for i in letters:  
  x = bin(i)
  checker = list(x)
  checker = map(int,checker[2:])
  if i > 128:
    i -= 128
  _sum = 0
  for j in checker:
    _sum += j
  if _sum % 2 == 0:
    result.append(chr(i))
print ''.join(map(str,result))  
  

