result = []
loops = int(raw_input())
for i in range(loops):
  counter = 0
  pages = 0
  printers = raw_input().split()
  printers = map(int, printers)
  while pages < printers[2]:
    counter += 1
    if counter % printers[0] == 0:
      pages += 1
      print '...'
    if counter % printers[1] == 0:
      pages += 1 
      print '...'    
  result.append(counter) 
print ' '.join(map(str,result))

