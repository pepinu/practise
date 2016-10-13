from math import atan as at, cos as c, sin as s, degrees as d, sqrt as p, radians as r
import operator

class Rot2D(object):
    def __init__(self):
        self.directions = []
        while 1:
            try:
                self.directions.append(raw_input())
            except:
                break

    @staticmethod
    def get_angle(x,y):
        try:
            ang = d(at(x/float(y)))
        except ZeroDivisionError:
            ang = 90 
        finally:   
            if y < 0:
                ang += 180  
            elif ang < 0 and y > 0 < x:
                ang += 180 
            return ang 

    @staticmethod
    def get_dist(Y,X):
        dist = p(X**2 + Y**2)
        return dist
    
    def solve(self):
        res = {} 
        result = []       
        p = [dire.split()[1] for dire in self.directions[:1]]
        angle = int(p[0]) 
        name = [dire.split()[0] for dire in self.directions[1:]]
        X = [int(dire.split()[1]) for dire in self.directions[1:]]
        Y = [int(dire.split()[2]) for dire in self.directions[1:]]
        for i in range(len(name)):
            d = self.get_dist(X[i], Y[i])
            a = self.get_angle(Y[i], X[i])
            a += angle
            new_x = round(d * c(r(a)))
            new_y = round(d * s(r(a)))
            res[name[i]] = new_y, new_x
        res = sorted(res, key=res.get)
        return ' '.join(map(str,res))


print Rot2D().solve() 


