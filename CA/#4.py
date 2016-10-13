result = []
loops = int(raw_input())
for i in range(loops):
    numbers = raw_input().split()
    numbers = map(int, numbers)
    if numbers[0] < numbers[1]:
        result.append(numbers[0])
    else:
        result.append(numbers[1])
        
print ' '.join(map(str,result))
