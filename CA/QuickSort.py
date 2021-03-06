class QuickSort(object):
    def __init__(self):
        self.inputs = []
        while 1:
            try:
                self.inputs.append(raw_input())
            except:
                break
    
    @staticmethod
    def partition(arr, left, right):
        lt = left
        rt = right
        _dir = 'left'  #specifies at which side currently empty space
        pivot = arr[left]
       
        while lt < rt:
            if _dir == 'left':
                if arr[rt] > pivot:
                    rt = rt - 1
                else:
                    arr[lt] = arr[rt]
                    lt += 1
                    _dir = 'right'
            else:   
                if arr[lt] < pivot:
                    lt += 1
                else:
                    arr[rt] = arr[lt]
                    rt += -1                
                    _dir = 'left'       
        arr[lt] = pivot     #here lt = rt - both >to[]cell 
        return lt 

    @staticmethod
    def qsort(self,arr, left, right, s):
        pivot_pos = self.partition(arr, left, right)
        x = str(left) + '-' + str(right)
        s.append(x)
        if pivot_pos - left > 1:
            self.qsort(self, arr, left, pivot_pos - 1,s)
        if right - pivot_pos > 1:
            self.qsort(self, arr, pivot_pos+1, right,s)
        return s
        

    def solve(self):
        d = [int(x) for x in self.inputs[1].split()]
        result = []
        s = []
        l = 0
        r = len(d)-1
        result = ' '.join(map(str,self.qsort(self,d,l,r,s)))
        return result

print QuickSort().solve()

