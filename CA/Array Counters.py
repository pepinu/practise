result = []
loops = raw_input().split()
loops = map(int, loops)
nums = raw_input().split()
nums = map(int, nums)
counter = []
x = loops[1] + 1
while loops[1] != 0:
    counter.append(0)
    loops[1] -= 1
for a in nums:
    for i in range(1, x):
        if i == a:
            counter[i-1] += 1
      
print " ".join(map(str, result))

