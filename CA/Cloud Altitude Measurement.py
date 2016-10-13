from math import tan as t, radians as r

class MeasureCloud(object):
    def __init__(self):
        self.inputs = []
        while 1:
            try:
                self.inputs.append(raw_input().split())
            except:
                break
    
    @staticmethod
    def calculate(d, A, B):
        H = (t(r(B)) * t(r(A)) * d)/ (t(r(B)) - t(r(A)))        
        return H 

    def solve(self):
        result = []
        for i in range(1,len(self.inputs)):
            self.inputs[i] = map(float, self.inputs[i])
            d = self.inputs[i][0]
            A = self.inputs[i][1]
            B = self.inputs[i][2] 
            result.append(int(round(self.calculate(d,A,B))))
        return ' '.join(map(str,result))
print MeasureCloud().solve()

