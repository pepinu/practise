result = []
loops = int(raw_input())
for i in range(loops):
    dices = raw_input().split()
    dices = map(float, dices)
    for a in dices:
        a *= 6
        a //= 1
        result.append(int(a) + 1)

print ' '.join(map(str,result))
    
