class Bogosort(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break

    @classmethod    
    def randomize(self, n):
        n = str(n).zfill(6)
        a = str(n)[:3]  
        b = str(n)[3:]
        if '' == a:
            a = '000'
        elif '' == b:
            b = '000'
            n = a+b
        Y = b+a
        n = long(n) * long(Y)
        n = str(n).zfill(12)
        n = n[3:9]
        return long(n)
     
    @classmethod
    def shuffle(self, nums):
        nums = nums.split()
        nums = map(int,nums)
        r = 918255
        c = 0
        x = 0
        while 0 == x:
            c += 1
            for i in range(len(nums)):
                r = self.randomize(r)
                j = r % len(nums)
                nums[i], nums[j] = nums[j], nums[i]
            if sorted(nums) == nums:
                x = 1
                return c
            if c > 50000:
                c = -1
                return c
    
    def solve(self):
        result = []
        for i in range(int(self.data[0])):
            result.append(self.shuffle(self.data[i+1]))
        return ' '.join(map(str, result))
    
print Bogosort().solve() 



