m=int(input())

memo=[[0 for X in range(5)] for x in range(1010)]

eng=[int(x) for x in input().split()]
memo[0][0]=0
memo[0][1]=eng[0]

for i in range(1,m):
    memo[i][0]=max(memo[i-1][0],memo[i-1][1],memo[i-1][2],memo[i-1][3],memo[i-1][4])
    memo[i][1]=memo[i-1][0]+eng[i]
    memo[i][2]=memo[i-1][1]+eng[i]
    memo[i][3]=memo[i-1][2]+eng[i]//2
    memo[i][4]=memo[i-1][3]+eng[i]//2

answer = max(memo[m-1][0],memo[m-1][1],memo[m-1][2],memo[m-1][3],memo[m-1][4])
print(answer)
