now=0
n, k=map(int, input().split())
k -= 1
answer=0

pizza = list(map(int, input().split()))



    mini = pizza.index(min(pizza))
    want = pizza
    if mini == k:
        now += mini+1
        break
    while True:
        now += mini+1
        if k>mini:
            k = k-mini-1
        for _ in range(mini):
            pizza.append(pizza[0])
            del pizza[0]
        del pizza[0]
    
print(now)
