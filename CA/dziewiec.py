result = []
vowels = ['a', 'o', 'u', 'i', 'e', 'y']
loops = int(raw_input())

for i in range(loops):
    count = 0
    words = raw_input().split()
    for a in words:
        for b in a:
            if b in vowels:
                count += 1
    result.append(count)

print ' '.join(map(str,result))
    
