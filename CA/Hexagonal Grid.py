from math import sqrt as p
def distance(x):
    return p(x[0]**2 + x[1]**2)

d = {
    'A': [1, 0], 
    'B': [0.5, p(3)/2], 
    'C': [-0.5, p(3)/2], 
    'D': [-1, 0], 
    'E': [-0.5, -p(3)/2], 
    'F': [0.5, -p(3)/2]
    }
result = []
times = input()
for i in range(times):
    pos = [0, 0]
    moves = raw_input()
    for j in moves:
        pos[0] += d[j][0]
        pos[1] += d[j][1]
    result.append(distance(pos))

print ' '.join(map(str,result))







