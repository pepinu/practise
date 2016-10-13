result = []
loops = int(raw_input())

for  i in range(loops):
  _vars = raw_input().split()
  _vars[0] = int(_vars[0])
  word = []
  for i in _vars[1]:
    word.append(i)

  if _vars[0] > 0:
    for i in range(_vars[0]):
      t = word[0]
      word.pop(0)
      word.append(t)
    result.append(str(''.join(word)))

  else:
    _vars[0] *= -1
    for i in range(_vars[0]):
      t = word[len(word)-1]
      word.pop()
      word.insert(0, t)
    result.append(str(''.join(word)))

print ' '.join(result)
