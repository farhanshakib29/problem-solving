def maxf(ara):
    max = 0
    for i in range(1, 5):
        max = max + ara[i]
    return max

def minf(ara):
    min = 0
    for i in range(0, 4):
        min = min + ara[i]
    return min
    
n = 5
ara = []

ara = list(map(int, input().split()))
ara.sort()

min = minf(ara)
max = maxf(ara)

print('%d %d' % (min, max))
