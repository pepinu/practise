from math import sqrt as p

X = []
Y = []
x = input()
for i in range(x):
    vertex = raw_input().split()
    vertex = map(int, vertex)
    X.append(vertex[0])
    Y.append(vertex[1])

At = 0
ref = [X[0], Y[0]]

for i in range(1,x-1):
    a = p((X[i] - ref[0])**2 + (Y[i] - ref[1])**2)
    b = p((X[i+1] - X[i])**2 + (Y[i+1] - Y[i])**2)
    c = p((ref[0] - X[i+1])**2 + (ref[1] - Y[i+1])**2) 
    s = (a + b + c) / 2
    A = p(s*(s-a)*(s-b)*(s-c))
    At += A
print At
