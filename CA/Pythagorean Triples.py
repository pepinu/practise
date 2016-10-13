def calc(x):
    a = 1
    b = 1

    for a in range(1,(x-2)/2):
        for b in range(1, (x-2)):
            for c in range(1,(x-2)) :
                print a, b+c, x-2-c         
                if a+ (b+c) + x-2-c == x and a**2 + (b+c)**2 == (x-2-c)**2:
                    return (x-2-c)**2  
                          
                

x = input()
for i in range(x):
    fir = input()
    print calc(fir)
  
  
