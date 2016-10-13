vowel = ['a', 'e', 'i', 'o', 'u',]
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p', 'r', 's', 't', 'v', 'w', 'x', 'z']
result = []

_input = raw_input().split()
_input = map(int, _input)
loops = _input[0]
X0 = _input[1]
nums = raw_input().split()
nums = map(int, nums)
A = 445
C = 700001
M = 2097152
for i in range(loops):
  word = []
  for a in range(nums[i]):
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
  result.append(x)
print ' '.join(map(str,result))    




