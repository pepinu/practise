import httplib2

class SaySto(object):
    def __init__(self):
        while 1:
            try:
                self.data = raw_input()
            except:
                break
    
    def solve(self):
        token = "token: " + self.data 
        http = httplib2.Http()
        while 1:
            response, content = http.request("http://codeabbey.sourceforge.net/say-100.php", "POST", token)     
            print content
            token += "\nanswer: " + raw_input()
print SaySto().solve() 


