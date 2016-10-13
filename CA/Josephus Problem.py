result = []
hld = []
loops = raw_input().split()
cnt = int(loops[1])
lms = range(1, int(loops[0])+1)

c = 0
while len(lms) != 1:
  hld = []
  for i in range(len(lms)):
    c += 1
    if c % cnt == 0 and c != 0:
      lms.insert(i, 'X')
      lms.pop(i+1)
    
  for a in lms:
    if str(a).isdigit():
      hld.append(a)  
  lms = hld
print ''.join(map(str, lms))

   
