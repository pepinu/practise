result = []
loops = int(raw_input())
for a in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    a = nums[0]
    b = nums[1]
    c = nums[2]
    check = a**2 + b**2
    if check > c**2:
        result.append('A')
    elif check == c**2:
        result.append('R')
    else:
        result.append('O')
print ' '.join(map(str,result))

