result = []
loops = int(raw_input())
for a in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    sum = 0
    cnt = 0
    while(nums[2] != 0):
        sum += nums[0] + nums[1]*cnt
        cnt += 1
        nums[2] -= 1
    result.append(sum)            
print ' '.join(map(str,result))

