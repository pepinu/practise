def suma(n, tlist):
    ls = []
    lim = 2 * n
    for i in xrange(0,lim,2):
        s = 0
        for j in range(2):
            s += tlist[i+j]
        ls.append(s)    
    print " ".join(map(str, ls))
    
a = 11
b = [572412, 907076, 467910, 286991, 622780, 796096, 351007, 156864, 39005, 635400, 919112,
 693172, 655987, 344780, 359373, 901202, 520649, 543296, 202820, 578107, 876405, 661381]

suma(a, b)
