result = []
p = input()
for i in range(p):
    z = 0
    c = 0
    ch = raw_input().split()
    ch = map(int, ch)
    ch[:] = [x*0.01000 for x in ch] 
    pA = ch[0]
    pB = ch[1]
    z =  ((pB)*(1-pA))
    for a in range(1,10):
        c += z        
        z *=  ((1-pB)*(1-pA))
        
    pA = (1 - c) * 100
    pA = round(pA)
    result.append(int(pA))
print ' '.join(map(str,result))
