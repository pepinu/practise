class CaesarCrack(object):

    def __init__(self):
        
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break

    @classmethod
    def getfreq(self, string, shift):

        freq = [0] * 26
        for i in range(len(string)):    
            if string[i] == ' ':
                continue            
            ind = (ord(string[i]) - ord('A') - shift) % 26
            freq[ind] += 1
        return freq

    @classmethod
    def checkdiff(self, freq, ideal):

        val = 0
        diff = [0] * 26
        for i in range(len(freq)):
            diff[i] = ideal[i] - freq[i]
            diff[i] **= 2
            val += diff[i]
        return val
   
    @classmethod
    def getwords(self,shift, string):
        spa, i = 0, 0
        cracked = []
        while spa != 3:
            if string[i] == ' ':
                cracked.append(' ')                
                spa += 1
            else:
                cracked.append(chr((ord(string[i]) - ord('A') - shift) % 26 + ord('A')))
            i += 1
        cracked.pop()
        return ''.join(map(str, cracked))
            
            
        
            

    def solve(self): 

        ideal = [8.1, 1.5, 2.8, 4.3, 
                 13.0, 2.2, 2.0, 6.1, 
                 7.0, 0.15, 0.77, 7.0, 
                 2.4, 6.8, 7.5, 1.9, 
                 0.095, 6.0, 6.3, 9.1, 
                 2.8, 0.98, 2.4, 0.15, 
                 2.0, 0.074]
        result = []
        messages = [x for x in self.data[1:]]
        for mes in messages:
            diffs = []
            for i in range(26):
                f = self.getfreq(mes,i)
                diffs.append(self.checkdiff(f, ideal))
            mini = diffs.index(min(diffs))
            result.append(self.getwords(mini, mes))
            result.append(mini)            
            
        return ' '.join(map(str,result))


print CaesarCrack().solve()
