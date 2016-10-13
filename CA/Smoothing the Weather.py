result = []
loops = int(raw_input())
data = raw_input().split()
data = map(float, data)
for i in range(len(data)):
  if i == 0 or i == len(data)-1:
    result.append(data[i])
  else:
    x =  (data[i-1] + data[i] + data[i+1])/3
    result.append(x)
            
print ' '.join(map(str,result))

