result = []
loops = int(raw_input())
days = 24 * 60 * 60
hours = 60* 60
minutes = 60
ans = []
for i in range(loops):
    numbers = raw_input().split()
    numbers = map(int, numbers)
    diff = 0 
    sum1 = 0
    sum2 = 0
    numbers[0] *= days
    numbers[4] *= days
    numbers[1] *= hours
    numbers[5] *= hours
    numbers[2] *= minutes
    numbers[6] *= minutes
    for i in range(4):
        sum1 += numbers[i]
    for i in range(4,8):
        sum2 += numbers[i] 
    diff = sum1 - sum2 
    if diff < 0:
        diff = -1 * diff
    a = diff // days
    diff %= days
    b = diff // hours
    diff %= hours
    c = diff // minutes
    diff %= minutes
    d = diff 
    res = [a, b, c, d]
    res = tuple(res)
    _str = "(" + ' '.join(map(str, res)) + ")"
    
    result.append(_str)
print ' '.join(map(str, result))
