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
        print num, base, d
        if 10 == base:
            nnum = [int(x) for x in str(num)]
            while len(nnum) < d:
                nnum.insert(0, 0)
            return nnum
        nnum = []
        while 0 != num:
            nnum.append(num%base)
            num /= base
        while len(nnum) < d:
            nnum.append(0)
        return nnum[::-1]

    @staticmethod
    def lucker(num):
        if len(num)%2 == 1:
            num.pop(len(num)/2)    
        a = sum(num[:len(num)/2])
        b = sum(num[len(num)/2:])
        if a == b:
            return 1
        return 0
            
    def solve(self):
        res = [0] * int(self.data[0])
        vals = [[int(x) for x in y.split()] for y in self.data[1:]]   
        dig = [x[0] for x in vals] 
        base = [y[1] for y in vals] 
        for times in range(len(dig)):
            i = 0
            while(len(self.convert(i,base[times],dig[times])) <= dig[times]):
                if 1 == self.lucker(self.convert(i, base[times],dig[times])):
                    res[times] += 1             
                i += 1
        return ' '.join(map(str,res))
     

print Tickets().solve() 


