choc = []
way = 0

n = int(input())
choc = list(map(int, input().split()))
d, m = map(int, input().split())

for i in range(n-m+1):
    sum = 0
    for j in range(i, i+m):
        sum = sum + choc[j]
    if sum==d:
        way = way + 1
        
print(str(way))
