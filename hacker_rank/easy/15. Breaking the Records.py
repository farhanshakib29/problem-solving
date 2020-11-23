def breakRec(game, n):
    
    maxs = game[0]
    mins = game[0]
    hig = 0
    low = 0
    
    for i in range(1, n):
        if game[i] > maxs:
            maxs = game[i]
            hig = hig + 1
    
    for i in range(1, n):
        if game[i] < mins:
            mins = game[i]
            low = low + 1
            
    print('%d %d' % (hig, low))

game = []

n = int(input())
game = list(map(int, input().split()))

breakRec(game, n)
