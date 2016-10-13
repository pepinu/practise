from math import radians as r, cos, sin

def solve(d, deg):
    x = 10.0 + d * sin(r(deg))
    y = 10.0 + d * cos(r(deg))
    return x, y

hdeg = 30
mdeg = 6
dh = 6
dm = 9
result = []
times = input()
time = raw_input().split()
for i in time:
    n = 0
    hour = []
    minute = []
    for j in i:
        if j == ':':
           n = 1        
        elif n == 0:
            hour.append(j)
        elif n == 1:
            minute.append(j)
    hour = ''.join(map(str,hour))
    hour = int(hour)
    minute = ''.join(map(str,minute))
    minute = int(minute)
    
    alpha = hour*hdeg + minute/60.0 * hdeg
    beta = minute*mdeg   
    result.append(" ".join(map(str, solve(dh, alpha))))
    result.append(" ".join(map(str, solve(dm, beta))))
print ' '.join(map(str,result))
