from math import sqrt
result = []
prime = []
positive = []
N = 3000000
loops = int(raw_input())
for i in range(N):
  positive.append(True)
i = 2

sieve = range(1, N)
positive[0] = False
positive[1] = False

while i*i <= N:
  if positive[i] == True:
    j = i*i
    while j < N:
      positive[j] = False
      j += i    
  i += 1

for i in range(len(positive)):
  if positive[i] == True:
    prime.append(i)

for j in range(loops):
  _range = raw_input().split(" ")
  _range = map(int, _range)
  for i in range(len(prime)):
    r = 1
    if prime[i] == _range[0]:
      while prime[i] != _range[1]:
        r += 1
        i += 1
      break
  result.append(r)

print ' '.join(map(str, result))

