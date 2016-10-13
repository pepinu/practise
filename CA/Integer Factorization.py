from math import sqrt
result = []
prime = []
positive = []
N = 300000

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

loops = input()
for i in range(loops):
  div = []
  nums = input()
  a = 0
  while nums not in prime: 
    while nums%prime[a] == 0 and nums != prime[a]:
      nums /= prime[a]
      div.append(prime[a])
    a += 1  
  div.append(nums)
  x = '*'.join(map(str,div))
  result.append(x)
print ' '.join(map(str,result))
