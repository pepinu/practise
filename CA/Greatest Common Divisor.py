result = []
loops = int(raw_input())
for i in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    lcm = nums[0] * nums[1]
    while nums[0] != nums[1]:
        if nums[0] > nums[1]:
            nums[0] -= nums[1]
        else:
            nums[1] -= nums[0]
    gcd = nums[1]
    lcm /= gcd
    res = [gcd, lcm]
    _str = "(" + ' '.join(map(str, res)) + ")"
    result.append(_str)
print ' '.join(map(str, result))
     

