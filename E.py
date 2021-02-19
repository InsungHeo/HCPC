import math as m
def nnn(n):
    o = int(m.sqrt(n))
    if o*o == n:
        return True
    else:
        return False

a=0
b=0
flag=False

n = int(input())
o = n%4
if o == 3:
    print(-1)
else:
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            print(-1)
            flag=True
            break

    if flag==False:
        for i in range(1, int(m.sqrt(n))+1):
            k = n-i*i
            if nnn(k):
                if a==0 and b==0:
                    a=i
                    b=int(m.sqrt(k))
                elif a+b>i+int(m.sqrt(k)):
                    a=i
                    b=int(m.sqrt(k))

        if a>b:
            a,b=b,a

        print(a,b)
