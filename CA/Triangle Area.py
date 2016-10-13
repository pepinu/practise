from math import sqrt as p
result = []
loops = int(raw_input())
for i in range(loops):
  nums = raw_input().split()
  nums = map(int, nums)
  a = p((nums[2] - nums[0])**2 + (nums[3] - nums[1])**2)
  b = p((nums[4] - nums[2])**2 + (nums[5] - nums[3])**2)
  c = p((nums[0] - nums[4])**2 + (nums[1] - nums[5])**2) 
  s = (a + b + c) / 2
  A = p(s*(s-a)*(s-b)*(s-c))
  result.append(A)    
print " ".join(map(str, result))

