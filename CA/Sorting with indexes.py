result = []
loops = int(raw_input())
x = raw_input().split()
x = map(int, x)
z = sorted(x)
for i in z:
  cnt = 0
  for j in x:
    cnt += 1
    if i == j:
      result.append(cnt)
print ' '.join(map(str,result))

