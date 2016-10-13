result = []
_sum = int(raw_input())
nums = raw_input().split()
while nums[0] != '%':
    if nums[0] == '+':
        _sum += int(nums[1])
    elif nums[0] == '*':
        _sum *= int(nums[1])
    nums = raw_input().split()
_sum %= int(nums[1])
result.append(_sum)      
print " ".join(map(str, result))

