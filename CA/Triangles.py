result = []
loops = int(raw_input())

for a in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    for i in nums:
        res = 1
        if nums[0] + nums[1] < nums[2]:
            res = 0
        if nums[0] + nums[2] < nums[1]:
            res = 0
        if nums[1] + nums[2] < nums[0]:
            res = 0
    result.append(res)
        
print ' '.join(map(str,result))

