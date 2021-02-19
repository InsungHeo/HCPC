n,m = map(int, input())
a = list(map(int, input()))
s = [[0]*n]*n
for i in range(m):
    x, y, z = map(int, input())
    s[x][y] = z
d = int(input())

def onedaylater(a, s):

    for i in range(len(a)):
        for j in range(len(a)):
            a[i] = a[j]*s[j][i]


for i in range(d):
    onedaylater(a, s)
for i in range(n):
    print(a[i])
