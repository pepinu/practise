result = []
loops = int(raw_input())
for i in range(loops):
    numbers = raw_input().split()
    numbers = map(int, numbers)
    mid = numbers[0]
    if numbers[1] < mid and numbers[2] < numbers[1]:
        mid = numbers[1]
    if numbers[1] > mid and numbers[2] > numbers[1]:
        mid = numbers[1]
    if numbers[2] < mid and numbers[1] < numbers[2]:
        mid = numbers[2]
    if numbers[2] > mid and numbers[1] > numbers[2]:
        mid = numbers[2]
    result.append(mid)
    
print ' '.join(map(str,result))

