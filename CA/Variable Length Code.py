class VarLenCode(object):
    
    def __init__(self):
        self.code = {
            ' ': '11',             'e': '101',
            't': '1001',           'o': '10001',
            'n': '10000',          'a': '011',
            's': '0101',           'i': '01001',
            'r': '01000',          'h': '0011',
            'd': '00101',          'l': '001001',
            '!': '001000',         'u': '00011',
            'c': '000101',         'f': '000100',
            'm': '000011',         'p': '0000101',
            'g': '0000100',        'w': '0000011',
            'b': '0000010',        'y': '0000001',
            'v': '00000001',       'j': '000000001',
            'k': '0000000001',     'x': '00000000001',
            'q': '000000000001',   'z': '000000000000',
        }

        self.directions = []
        while 1:
            try:
                self.directions.append(raw_input())
            except:
                break

    @staticmethod
    def to_hex(x):
        h = "%X" % int(x,2)
        return h.zfill(2)   

    def solve(self):
        result = []
        pref = []
        x = []
        d = [dire for dire in self.directions]

        for i in range(len(d[0])):
            x.append(self.code[d[0][i]])
        x = ''.join(map(str,x))
        n = len(x)/8

        for j in range(n + 1): 
            temp = [] 
            try:  
                for i in range(8):
                    temp.append(x[i + j*8])
            except:
                break
            finally:
                pref.append(''.join(map(str,temp)))
        pref[-1] = pref[-1][::-1]
        pref[-1] = pref[-1].zfill(8)
        pref[-1] = pref[-1][::-1]
        for i in range(len(pref)):
            result.append(self.to_hex(pref[i]))
        return ' '.join(map(str,result))
        
  
print VarLenCode().solve() 


