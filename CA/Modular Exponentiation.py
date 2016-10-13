class ModExp(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break

    @classmethod
    def binarize(self, x,y,z):
        s = 1
        c = bin(x)
        c = c[2::]
        for i in range(len(c)):
            if c[i] == '0':
                continue
            s *= int(c[i])* y**(2**(len(c)-1-i)) %z
        return s 

    @classmethod
    def recursive(self,x,y,z):
        if x == 0:
            return 1
        if x == 1:
            return y%z
        elif x%2 == 0:
            return self.recursive(x/2, y*y%z, z) %z
        else:
            return y * self.recursive(x/2, y*y%z, z) %z        
    
    def solve(self):
        result = []
        base = [int(d.split()[0]) for d in self.data[1:]]
        exponent = [int(d.split()[1]) for d in self.data[1:]]
        modulo = [int(d.split()[2]) for d in self.data[1:]]
        for i in range(len(base)):
            result.append(self.recursive(exponent[i], base[i], modulo[i]))
        return ' '.join(map(str, result))
    
print ModExp().solve() 


