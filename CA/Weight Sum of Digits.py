result = []
loops = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)
for a in nums:
    wsd = 0
    co = 1
    while(a != 0):
        cin = 1
        temp = a
        while(a >= 10):
            a /= 10
            cin += 1
        wsd += a * co
        co += 1
        if (temp - a * 10**(cin-1) < 10**(cin-3)):
            co += 2
        elif(temp - a * 10**(cin-1) < 10**(cin-2)):
            co += 1
        a = temp - a * 10**(cin-1)
    result.append(wsd)
        
print ' '.join(map(str,result))

