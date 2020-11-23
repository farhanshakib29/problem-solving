def getTotalX(a, b, m, n):

    am = a[m-1]
    b0 = b[0] + 1
    l = []
    q = 0
    
    for i in range(am, b0):
        p = 0
        for j in range(m):
            if i%a[j] == 0:
                p = p + 1
        if p == m:
            l.append(i)

    ll = len(l)
    
    for i in range(ll):
        p = 0
        for j in range(n):
            if b[j] % l[i] == 0:
                p = p + 1
        if p == n:
            q = q + 1
                
    print(str(q))

a = []
b = []

m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

getTotalX(a, b, m, n)
