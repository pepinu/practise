from math import tan as t, radians

result = []
x = input()
for i in range(x):
    mes = raw_input().split()
    mes = map(float, mes)
    H = mes[0] * t(radians(mes[1] - 90))
    result.append(int(round(H)))
print ' '.join(map(str,result))
