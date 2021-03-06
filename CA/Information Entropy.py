import math, string

class Entropy(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
    
    def get_freq(self, passed_string):
        res = []
        alpha = [0] * (len(string.ascii_lowercase) + 1)
        leng = float(len(passed_string))
        for i in passed_string:
            if i in string.ascii_lowercase:
                alpha[ord(i)-ord('a')] += 1
            else:
                alpha[-1] += 1
        for i in alpha:
            if i != 0:
                res.append(i/leng)
        return res

        

    def get_entropy(self, freq):
        result = 0
        for i in freq:
            result += (i * (-1*math.log(i,2)))
        return result
            
                   
    def solve(self):
        res = []    
        words = [y for y in self.data[1:]]
        for i in range(len(words)):
            res.append(self.get_entropy(self.get_freq(words[i].lower())))
        return ' '.join(map(str,res))

print Entropy().solve() 


