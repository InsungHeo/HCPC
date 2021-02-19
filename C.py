k=int(input())

while(k):
    binary = input()
    flag=0

    rebinary = binary[::-1]
    if(binary!=rebinary):
        flag+=1

    n= int("0b"+binary,2)

    eight = oct(n)
    six = hex(n)

    eight=eight[2:]
    six=six[2:]

    reeight=eight[::-1]
    resix=six[::-1]

    if(reeight!=eight):
        flag+=1
    if(resix!=six):
        flag+=1



    if(flag<=1):
        print('yes')
    else:
        print('no')
    k-=1
