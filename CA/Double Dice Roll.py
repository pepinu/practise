result = []
loops = int(raw_input())
for i in range(loops):
    _sum = 0
    dices = raw_input().split()
    dices = map(float, dices)
    for a in dices:
        a %= 6
        a += 1
        _sum += a
    result.append(int(_sum))

print ' '.join(map(str,result))
    
