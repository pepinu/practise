result = []
for i in range(3):
    data = raw_input().split()
    data.pop()
    data = map(float, data)
    nos = int(round(max(data)/min(data)))
    nod = int(min(data))
    r = nod, "d" ,nos    
    result.append(''.join(map(str,r)))
print ' '.join(map(str,result))

