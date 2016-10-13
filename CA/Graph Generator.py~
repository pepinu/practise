class GraphGen(object):
    def __init__(self):
        self.data = []
        while 1:
            try:
                self.data.append(raw_input())
            except:
                break 


    @classmethod
    def randomize(self, N, X0): 
        result = []
        for i in range(N):
            X = (445 * X0 + 700001) % 2097152
            X0 = X
            Y = X % N + 1
            result.append(Y)
        return result

    def solve(self):    
        result = []
        params = [int(y) for y in self.data[0].split()]
        return self.randomize(params[0], params[1])

print GraphGen().solve()
