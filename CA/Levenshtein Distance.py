class ModExp(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break

    @classmethod    
    def levdis(self,a,b):
        if len(a) > len(b):
            a,b = b,a
            print a, b
        dis = range(len(a)+1)
        for ind,ch in enumerate(b):
            print ind, ch
            ndis = [ind+1]
            for ind1,ch1 in enumerate(a):
                if ch1 == ch:
                    ndis.append(dis[ind1])
                    print ndis
                else:
                    ndis.append(1 + min(dis[ind1], dis[ind1+1], ndis[-1]))
                    print ndis
            dis = ndis
        return dis[-1]
                    
    
    def solve(self):
        result = []
        fword = [d.split()[0]  for d in self.data[1:]]
        sword = [d.split()[1] for d in self.data[1:]]
        for i in range(len(fword)):
            result.append(self.levdis(fword[i],sword[i]))
        return ' '.join(map(str,result))
    
print ModExp().solve() 


