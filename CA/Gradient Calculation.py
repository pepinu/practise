import math

class Gradient(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
        
    @staticmethod
    def f(x, y, A, B, C): 
        return (x  - A)**2 + (y - B)**2 + C * math.exp( - (x + A)**2 - (y + B)**2)

    @classmethod
    def grad(self,x,y, p):
        dt = 1e-9    
        a = self.f(x,y, p[1], p[2], p[3])
        b = self.f(x+dt ,y, p[1], p[2], p[3])
        c = self.f(x, y+dt, p[1], p[2], p[3])
        return int(round(math.degrees(math.atan2((c-a)/dt,(b-a)/dt)))) + 180

            
    def solve(self):
        res = []
        para = [float(x) for x in self.data[0].split()]
        vals = [[float(x) for x in y.split()] for y in self.data[1:]]         
        for val in vals:
            res.append(self.grad(val[0], val[1], para))
        return ' '.join(map(str,res))
     

print Gradient().solve() 

