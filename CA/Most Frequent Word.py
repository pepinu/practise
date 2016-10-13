import operator

vowel = ['a', 'e', 'i', 'o', 'u',]
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p', 'r', 's', 't', 'v', 'w', 'x', 'z']
result = {}
A = 445
C = 700001
M = 2097152

def WC(X0):
  r = None
  for i in range(900000):
    word = []
    for a in range(6):
      if a % 2 == 1:
        mod = 5
        ind = 0
      else:
        mod = 19
        ind = 1
      X = (A * X0 + C) % M
      L = X % mod
      if ind == 1:
        word.append(consonant[L])
      else:
        word.append(vowel[L])
      X0 = X
    x = ''.join(map(str,word))
    if x in result:
      result[x] += 1
    else:
      result[x] = 1
  return max(result.iteritems(), key=operator.itemgetter(1))[0]
X0 = input()
print WC(X0)


    




