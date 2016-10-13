result = []
loops = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)
for i in nums:
  count = 0
  x = bin(i & 0b11111111111111111111111111111111)
  x = list(x)
  for i in range(2):
    x.pop(0)
  x = map(int, x)
  for i in x:
    count += i
  result.append(count)
print ' '.join(map(str,result))
