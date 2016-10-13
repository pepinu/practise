import numpy

def solve(a, b):
  std = numpy.std(b)
  mean = numpy.mean(b)
  com = 0.01 * round(mean)
  if com * 4 < std:
    return a
  
times = input()
result = []
for i in range(times):
  stock = raw_input().split()
  name = stock[0]
  stock = map(int, stock[1::])
  if solve(name,stock) != None:
    result.append(solve(name, stock))
print ' '.join(map(str,result))
