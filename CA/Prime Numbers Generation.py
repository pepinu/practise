result = []

prime = []
loops = int(raw_input())
primes = raw_input().split(" ")
primes = map(int, primes)

for i in range(2,200000):
  x = 0 
  for p in range(2, i):
    if i % p == 0 and i != p:
      x = 1 
  if x == 0:
    prime.append(i) 

for i in primes:
  result.append(prime[i])

print ' '.join(map(str, result))

