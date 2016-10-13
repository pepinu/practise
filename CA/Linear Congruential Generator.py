result = []
loops = int(raw_input())
X = 0
for i in range(loops):
  nums = raw_input().split()
  nums = map(int, nums)
  A = nums[0]
  C = nums[1]
  M = nums[2]
  X0 = nums[3]
  N = nums[4]
  for i in range(N):
    X = (A * X0 + C) % M
    X0 = X
  result.append(X)

print ' '.join(map(str,result))

