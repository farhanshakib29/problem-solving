def match(x1, v1, x2, v2):
    for i in range(10001):
        x1 = x1 + v1
        x2 = x2 + v2
        
        if(x1 == x2):
            print('YES')
            return
            
    print('NO')

x1, v1, x2, v2 = map(int, input().split())
match(x1, v1, x2, v2)
