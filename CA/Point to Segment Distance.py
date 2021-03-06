from numpy import dot
from math import sqrt as p

class DistToSeg(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break

    @staticmethod
    def createvec(x1,y1, x2,y2):
        v = [x2-x1, y2-y1, 0]
        print v
        return v

    @staticmethod
    def comparev(v1,v2):
        r = dot(v1, v2) 
        return r  

    @staticmethod
    def distance(x1,y1, x2,y2):
        d = p((x2- x1)**2 + (y2 - y1)**2)   
        return d

    def solve(self):
        result = []
        x1 = [float(d.split()[0]) for d in self.data[1:]]
        y1 = [float(d.split()[1]) for d in self.data[1:]]
        x2 = [float(d.split()[2]) for d in self.data[1:]]
        y2 = [float(d.split()[3]) for d in self.data[1:]]
        xp = [float(d.split()[4]) for d in self.data[1:]]
        yp = [float(d.split()[5]) for d in self.data[1:]] 
        for i in range(len(x1)):  
            f = self.createvec(x1[i],y1[i],x2[i],y2[i])
            ff = self.createvec(x2[i],y2[i],x1[i],y1[i])
            s = self.createvec(x1[i],y1[i],xp[i],yp[i])
            t = self.createvec(x2[i],y2[i],xp[i],yp[i])
            a1 = self.comparev(f,s) 
            a2 = self.comparev(ff,t)
            if a1 <= 0:
                result.append(self.distance(x1[i],y1[i],xp[i],yp[i]))
            elif a2 <= 0:
                result.append(self.distance(x2[i],y2[i],xp[i],yp[i]))
            else:   
                result.append(abs((y1[i]-y2[i])*xp[i] - (x1[i]-x2[i])*yp[i] + x1[i]*y2[i] - y1[i]*x2[i])/p((y1[i]-y2[i])**2 + (x1[i]-x2[i])**2))
        return ' '.join(map(str, result))        
     
     
        

print DistToSeg().solve() 


