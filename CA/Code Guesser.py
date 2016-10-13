result = [None,None,None]
loops = input()
guesso = []
guessf = []
for i in range(loops):
  nums = raw_input().split()
  nums = map(int, nums)
  if nums[1] == 2:
    guesso.append(nums[1])
  if nums[1] == 1:
    guessf.append(nums[1])
  
for i in guessf:
  if None not in result:
    break
  for j in guessf:
 
