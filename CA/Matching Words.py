result = []
store = []
nums = raw_input().split()
for i in nums:
  if i not in store:
    store.append(i)
  elif i not in result:
    result.append(i)
  else:
    continue
  result = sorted(result)
print ' '.join(map(str,result))

