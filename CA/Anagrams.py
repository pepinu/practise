import itertools
def solve_anagrams(x,d):
  check = []
  r = -1
  p = itertools.permutations(x)
  for i in p:
    word = []
    if i not in check:
      word.append(''.join(map(str, i)))
    if "".join(word) in d:
      r += 1  
    check.append(i)
  return r

d = []
with open("words.txt") as f:
    for line in f:
       d.append(line[:-2])
result = []
times = input()
for i in range(times):
  x = raw_input()
  result.append(solve_anagrams(x,d))
print ' '.join(map(str,result))
