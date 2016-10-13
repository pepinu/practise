result = []
loops = int(raw_input())
for i in range(loops):
  nums = raw_input().split()
  nums = map(int, nums)
  point = (float(nums[0] * nums[1]))/(float(nums[1] + nums[2]))
  result.append(point)        
print ' '.join(map(str,result))

