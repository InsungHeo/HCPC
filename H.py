import math

cnt = 0
pw = 0
N = int(input())
x = [0]*N
y = [0]*N
d = [0]*N
t = [0]*N
ts = [0]*N
sb = [0]*N
m = [0]*N

for i in range(N):
    x[i], y[i] = map(int, input().split())
    d[i] = math.sqrt(x[i]**2 + y[i]**2)
    t[i] = x[i]/y[i]

ts = t.sort()
m = [int(t.index(ts[i])) for i in range(N)]

for i in range(N):
    if pw < d[m[i]]:
        cnt += 1
        pw = d[m[i]]
        if m[i] == m[i+1]:
            d[i+1] = 0

print(cnt)
