result = []
loops = int(raw_input())
for i in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    a = (nums[3] - nums[1])/(nums[2] - nums[0])
    b = (nums[1] - a * nums[0])

    res = [a, b]
    _str = "(" + ' '.join(map(str, res)) + ")"
    result.append(_str)
print ' '.join(map(str, result))



