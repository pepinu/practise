result = []
loops = int(raw_input())
for a in range(loops):
    nums = raw_input().split()
    nums = map(int, nums)
    cnt = 0;
    sum = 0;
    for i in nums:
        if not i == 0:
            sum += i
            cnt += 1
        else:
            avg = round(float(sum)/cnt)
    result.append(int(avg))
        
print ' '.join(map(str,result))

