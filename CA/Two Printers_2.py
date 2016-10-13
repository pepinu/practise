result = []
loops = int(raw_input())
for i in range(loops):
  counter = 0
  pages = 0
  printers = raw_input().split()
  printers = map(int, printers)
  cc = 0
  while pages < printers[2]:
    if printers[0] < printers[1]:
      a = printers[0]
      b = printers[1]
    elif printers[0] > printers[1]:
      a = printers[1]
      b = printers[0]
    else:
      counter = float(round(printers[0])/2.0 * printers[2])
      break
    counter += a
    pages += 1
    if counter // b > cc: 
      pages += 1 
      cc += 1
    if printers[2] - pages == 1:
      while True:
        counter +=1
        if counter % a == 0:
          pages += 1
        if counter % b == 0:
          pages += 1
        if pages == printers[2]:
          break
  result.append(int(counter)) 
print ' '.join(map(str,result))

