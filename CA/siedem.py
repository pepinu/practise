result = []
loops = int(raw_input())

for i in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    ans = nums[0] / nums[1]
    mod = nums[0] % nums[1]
    mod = float(mod) / float(nums[1])
    if mod >= 0.5:
        ans += 1
    result.append(ans)

print ' '.join(map(str,result))

