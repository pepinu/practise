result = []
brackets_l = ['(',  '[',  '{',  '<']
brackets_r = [')',  ']',  '}',  '>']
loops = int(raw_input())
for i in range(loops):
  data = []
  nums = raw_input().split()
  for i in nums:
    for j in i:
      if j in brackets_l :
          data.append(j)
      elif j in brackets_r:
          data.append(j)
  data.append(' ')   
  cnt = 0
  while len(data) > 2 and cnt < 20000:
    x = len(data) -1 
    i = 0
    while i < x :
      
      if data[i] == brackets_l[0] and data[i+1] == brackets_r[0]:
        
        del data[i+1]
        del data[i]
      if data[i] == brackets_l[1] and data[i+1] == brackets_r[1]:
        
        del data[i+1]
        del data[i]
      if data[i] == brackets_l[2] and data[i+1] == brackets_r[2]:
        
        del data[i+1]
        del data[i]
      if data[i] == brackets_l[3] and data[i+1] == brackets_r[3]:
        
        del data[i+1]
        del data[i]
     
      i += 1
      cnt += 1
      x = len(data) -2
     
  if len(data) == 1:
    result.append(1)
  else:
    result.append(0)
  print data
print ' '.join(map(str, result))


