result = []
list = raw_input().split()
min = int(list[0])
max = int(list[0])

for i in range(len(list)):
    if int(list[i]) < min:
        min = int(list[i]) 
    if int(list[i]) > max:
        max = int(list[i]) 

result.append(max)
result.append(min)

    
print ' '.join(map(str,result))

