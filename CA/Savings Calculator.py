result = []
percent = 0.01
loops = int(raw_input())
for i in range(loops):
    data = raw_input().split()
    data = map(float, data)
    Y = 0
    S = float(data[0])
    R = data[1]
    P = percent * data[2] + 1
    while S < R:
        S *= P
        Y += 1
        print S
    result.append(int(Y))

print ' '.join(map(str,result))
    
