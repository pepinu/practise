
result = []
loops = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)
cnt_in = 1
cnt_out = 0
p = 0
for i in range(len(nums)):
  for j in range(i):
    if nums[i] < nums[j]:
      cnt_out += 1
      t = nums[j]
      nums[j] = nums[i]
      nums[i] = t
      p = 1

  if p == 1:
    cnt_in += 1    
    p = 0
      
result.append(cnt_in)
result.append(cnt_out)
 
print " ".join(map(str, result))

