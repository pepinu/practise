result = []
loops = int(raw_input())
for i in range(loops):
    numbers = raw_input().split()
    numbers = map(int, numbers)
    min = numbers[0]
    if numbers[1] < min
        min = numbers[1]
    if numbers[2] < min
        min = numbers[2]
    result.append(min)
    
print ' '.join(map(str,result))

