import string
cba = abc = string.ascii_uppercase
abc = list(abc)
cba = list(cba)
result = []
_input = raw_input().split()
_input = map(int, _input)
for i in range(_input[1]):
  t = abc[0]
  abc.pop(0)
  abc.append(t)
for a in range(_input[0]):
  words = raw_input().split("\n")
  for i in words:
    cphr = []
    for j in i:
      if j in abc:
        x = abc.index(j)
        cphr.append(cba[x])
      elif j == ' ':
        cphr.append(' ')
      elif j == '.':
        cphr.append('.')
    x = ''.join(map(str,cphr)) 
    result.append(x)
print ' '.join(map(str, result))
      
