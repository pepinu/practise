from math import sin as s, cos as c, radians as r

class Azimuth(object):
    def __init__(self):
        self.directions = []
        while 1:
            try:
                self.directions.append(raw_input().split())
            except:
                break

    @staticmethod
    def get_x(d, az):
        X = d * s(r(az))
        return X  

    @staticmethod
    def get_y(d,az):
        Y = d * c(r(az))
        return Y
    
    def solve(self):
        result = [0, 0]
        d = [int(dire.split()[1]) for dire in self.directions[1:-1]]
        az = [int(dire.split()[5]) for dire in self.directions[1:-1]]
        for i in range(len(d)):
            result[0] += self.get_x(d[i], az[i])
            result[1] += self.get_y(d[i], az[i])
        result[0] = int(round(result[0]))
        result[1] = int(round(result[1]))
        return ' '.join(map(str, result))
    
print Azimuth().solve() 


