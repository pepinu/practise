class PitchnNotes(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
        
    @staticmethod
    def calc(x,y):
        dc = x - 10
        dn = int(y) - 4
        r = 440 * (2**dn) * (2**(dc/12.0))
        return int(round(r))

    def solve(self):
        data = {
                'C':1,  
                'C#':2,
                'D':3,
                'D#':4,  
                'E':5,
                'F':6,  
                'F#':7,  
                'G':8,
                'G#':9,
                'A':10,
                'A#':11,
                'B':12,
                 }
        res = []
        vals = [[x for x in y] for y in self.data[1].split()]
        for i in range(len(vals)):
            if vals[i][1] == '#':
                vals[i][0] = vals[i][0] + vals[i][1]
                vals[i][1] = vals[i][2]
                vals[i].pop()
            res.append(self.calc(data[vals[i][0]], vals[i][1]))                   
        return ' '.join(map(str,res))
     

print PitchnNotes().solve() 


