result = []
loops = int(raw_input())
for i in range(loops):
  sum = 0
  nums = raw_input().split()
  nums = map(int, nums)
  for i in nums:
    sum += i**2
  result.append(sum)
print ' '.join(map(str, result))


