def qmark(algo):
    l = []
    _sum = 0
    for index, item in enumerate(algo):
        if item == '?':
            i_of_q = index
            l.append(0)
        else:
            l.append(item)
    l = map(int, l)
    t = map(int, l)
    for i in range(len(t)):
        if i % 2 == 0:
            t[i] *= 2  
            if t[i] > 9:
                t[i] -= 9
    for i in t:
        _sum += i
    if _sum % 10 != 0 :
        x = 10 - (_sum % 10)
        if x % 2 == 1 and i_of_q % 2 == 0:
            x += 9
            x /= 2
        elif i_of_q % 2 == 0:
            x /= 2  
        l.pop(i_of_q)
        l.insert(i_of_q, x)
    l = ''.join(map(str,l))
    return l 

def swap(algo):
    i = 0
    l = []
    for item in algo:
        l.append(item)
    l = map(int,l)
    t = map(int,l)
    x = map(int,t)
    while True:
        temp = t[i]
        t[i] = t[i+1]
        t[i+1] = temp
        for j in range(len(t)):
            if j % 2 == 0:
                t[j] *= 2  
                if t[j] > 9:
                    t[j] -= 9
        if sum(t) % 10 == 0:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            l = ''.join(map(str,l))
            return l
        i += 1
        t = map(int,x)

        
result = []
times = int(raw_input())
for i in range(times):    
    algo = raw_input()
    if '?' not in algo:
        result.append(swap(algo)) 
    else:
        result.append(qmark(algo))  
print ' '.join(map(str,result))
