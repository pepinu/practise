result = []
loops = int(raw_input())
for i in range(loops):
    suma = 0;
    smdg = raw_input().split()
    smdg = map(int, smdg)
    a = smdg[0] * smdg[1] + smdg[2]  
    while(a != 0):
        suma += a % 10
        a //= 10
    result.append(suma)

print ' '.join(map(str,result))

