class Tickets(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
    
    @staticmethod    
    def convert(num,base,d):
#        print num, base, d
        if 10 == base:
            nnum = [int(x) for x in str(num)]
            while len(nnum) < d/2:
                nnum.insert(0, 0)
            return nnum
        nnum = []
        while 0 != num:
            nnum.append(num%base)
            num /= base
        while len(nnum) < d/2:
            nnum.append(0)
        return nnum[::-1]

            
    def solve(self):
        res = [0] * int(self.data[0])
        vals = [[int(x) for x in y.split()] for y in self.data[1:]]   
        dig = [x[0] for x in vals] 
        base = [y[1] for y in vals] 
        for times in range(len(dig)):
            i = 0
            suma = [0] * (((base[times]-1) * dig[times]) + 2) 
            while(len(self.convert(i,base[times],dig[times])) <= (dig[times]+1)/2):
                suma[sum(self.convert(i, base[times],dig[times]))] += 1 
                i += 1
            print suma
#            for index in range(len(suma)):
#                suma[index] **= 2

            res[times] = sum(suma)
        return ' '.join(map(str,res))
     

print Tickets().solve() 


