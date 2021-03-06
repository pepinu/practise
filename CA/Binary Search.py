from math import sqrt, exp

def solve(A, B, C, D):
  left = 0
  right = 100
  mid =  50
  while True:
    one = A*left + B*sqrt(left**3) - C*exp(-left/50) - D 
    two = A*right + B*sqrt(right**3) - C*exp(-right/50) - D 
    three = A*mid + B*sqrt(mid**3) - C*exp(-mid/50) - D
    print "three", three
    if three < 0.000000001 and three > 0:
      return mid
    elif three > 0 and one < 0:
      right = mid
      mid = (left+right)/2.0
    elif three < 0 and two > 0:
      left = mid
      mid = (left+right)/2.0
    

result = []
loops = int(raw_input())
for i in range(loops):
  coeff = raw_input().split()
  coeff = map(float, coeff)
  A, B, C, D = coeff[0], coeff[1], coeff[2], coeff[3]
  result.append(solve(A,B,C,D))
  
  
print ' '.join(map(str, result))


