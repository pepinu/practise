loops = int(raw_input())
result = []
for i in range(loops):
  pali = raw_input()
  _list = []
  for i in pali:
    ans = 'N'
    if i.isalpha():
      i = i.lower()
      _list.append(i)
    else:
      continue

  first = _list[:len(_list)/2]
  first = first[::-1]
  if len(_list) % 2 == 1:
    second = _list[(len(_list)/2 +1):]
  else:
    second = _list[(len(_list)/2):]
  if first == second:
    ans = 'Y'
  result.append(ans)

print ' '.join(result)

