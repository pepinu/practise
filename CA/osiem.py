result = []
numbers = raw_input().split()
numbers = map(int, numbers)
for i in range(1, numbers[0] + 1):
    celc = ( numbers[i] - 32 ) / 1.8 
    r = celc % int(celc)
    if r > 0.5:
        celc += 1
    result.append(int(celc))

print ' '.join(map(str,result))
    
