class Problem121(object):
    """Insertion Sort"""
    def __init__(self):
        self.lines = []
        while 1:
            try:
                self.lines.append(raw_input())
            except:
                break

    def solve(self):
        shifts = []
        nums = [int(x) for x in self.lines[1].split()]
        result = nums[:1]
        for x in nums[1:]:
            found = None
            for i, v in enumerate(result):
                if v > x:
                    found = i
                    break
            if found is not None:
                shifts.append(len(result) - i)
                result.insert(i, x)
            else:
                shifts.append(0)
                result.append(x)
        return ' '.join([str(x) for x in shifts])


print Problem121().solve()
