class BuildTree(object):
    def __init__(self):
        self.data = []        
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
    
    @classmethod
    def compare(self,x,y,i):
        if x > y[i] and y[i+2] == '-':
            d = 5
            if len(y) > i+d+3 and type(y[i+d]) != int:
                while type(y[i+d]) != int:
                    d+=1
            if len(y) > i+d and x > y[i+d] and type(y[i+d]) == int :
                self.compare(x,y,i+d)
            else:
                del y[i+2]   
                y.insert(i+2,')')
                y.insert(i+2,'-')
                y.insert(i+2,',')
                y.insert(i+2, x)
                y.insert(i+2,',')
                y.insert(i+2,'-')
                y.insert(i+2,'(')  
   
        elif x >= y[i]:
             while type(y[i+4]) != int: 
                i+=1        
             self.compare(x,y,i+4)

            
        elif x < y[i] and y[i-2] == '-':
            d = 5            
            if i > d and type(y[i-d]) != int:
                while type(y[i-d]) != int:
                    d += 1
            if i > d and  x < y[i-d]:
                self.compare(x,y,i-d)
            else:          
                del y[i-2]
                y.insert(i-2,')')
                y.insert(i-2,'-')
                y.insert(i-2,',')
                y.insert(i-2,x)
                y.insert(i-2,',')
                y.insert(i-2,'-')
                y.insert(i-2,'(')

        elif x <= y[i]:
             while type(y[i-4]) != int: 
                i-=1        
             self.compare(x,y,i-4)
        else:
            return 
        

            
    
    @classmethod
    def instotree(self, x, g): 
        for i in range(len(x)):
            if i == 0:
                g.append('(')
                g.append('-')
                g.append(',')
                g.append(x[i])
                g.append(',')
                g.append('-')
                g.append(')')
            else:
                self.compare(x[i],g,g.index(x[0]))
        return g
                
    
    def solve(self):
        result = []
        vals = [int(x) for x in self.data[1].split()]
        return ''.join(map(str,self.instotree(vals, result)))
     

print BuildTree().solve() 


