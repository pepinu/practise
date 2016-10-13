n = int(input())

for i in range(n):
    
    nums = [int(j) for j in input().split(" ")]
    x, y, n = nums[0], nums[1], nums[2]
    
    t = (x * y * n) // (x+y)
    
    while t//x + t//y < n:
        t = t + 1
    
    print(t)
    print(" ")
