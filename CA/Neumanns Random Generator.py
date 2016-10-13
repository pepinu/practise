result = []

loops = int(raw_input())
nums = raw_input().split()
nums = map(int, nums)
for i in nums:
  loop = [str(i).zfill(4)]
  while True:
    i = int(i) ** 2
    i = str(i).zfill(8)
    i = i[2:6]
    i = i.zfill(4)
    if i in loop:
      result.append(len(loop))
      break
    else:
      loop.append(i)

print ' '.join(map(str,result))

