import itertools, math

class fPoW(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
    
    def chdict(self,d, leng):
        nd = []
        for i in range(len(d)):
            if len(d[i]) == leng:
                nd.append(d[i])
        return nd

    def count(self, leng,letters,d):
        r = 0
        
        for i in d:
            t = []
            x = 0
            for letter in letters:
                t.append(letter)
            for j in i:
                if j in t:
                    x += 1
                    t.pop(t.index(j))
                if leng == x:
                    r += 1
        return r
            
                   
    def solve(self):
        res = []
        d = []
        with open("words.txt") as f:
            for line in f:
                d.append(line[:-2])   
        leng = [int(y.split()[0]) for y in self.data[1:]]
        letters = [[x for x in y.split()[1:]] for y in self.data[1:]]
        for i in range(len(letters)):
            res.append(self.count(leng[i],letters[i],self.chdict(d,leng[i])))
       
        return ' '.join(map(str,res))
     

print fPoW().solve() 


