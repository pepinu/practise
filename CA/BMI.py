result = []
loops = int(raw_input())

for i in range(loops):
    inp = raw_input().split()
    inp = map(float, inp)
    BMI = inp[0] / inp[1]**2
    if BMI < 18.5:
        result.append('under')
    if 18.5 <= BMI < 25.0:
        result.append('normal')
    if 25.0 <= BMI < 30.0:
        result.append('over')
    if 30.0 <= BMI: 
        result.append('obese')

print ' '.join(result)
