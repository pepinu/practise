from math import floor 

class BinaryHeap(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break
    

    @classmethod
    def heapswap(self, Ar, k, leng):
        left = 2*k   
        right = 2*k+1
        smallest = None
        if left < leng and Ar[left] < Ar[k] :
            smallest = left 
        else:
            smallest = k
        if right < leng and Ar[right] < Ar[smallest]: 
            smallest = right
        if smallest != k:
            print Ar
            Ar[k], Ar[smallest] = Ar[smallest], Ar[k]
            self.heapswap(Ar, smallest, leng)

    @classmethod
    def swappar(self,Ar,k):
        pass
    @classmethod
    def delmin(self, Ar):
        k = 0
        while 1:
            try:
                if Ar[2*k+1] < Ar[2*k+2]:
                    Ar[k], Ar[2*k+1] = Ar[2*k+1], Ar[k]
                    k = 2*k+1
                else:   
                    Ar[k], Ar[2*k+2] = Ar[2*k+2], Ar[k]
                    k = 2*k+2
                
            except IndexError:
                Ar.pop(k)
                break
        

    def solve(self):
        leaves = [int(x) for x in self.data[1].split()]
        for i in range(len(leaves)):
            if leaves[i] == 0: 
                leaves.pop(i)      
                self.delmin(leaves)
            else:
                self.heapswap(leaves, i, len(leaves))
        return ' '.join(map(str,leaves))
    
print BinaryHeap().solve() 


