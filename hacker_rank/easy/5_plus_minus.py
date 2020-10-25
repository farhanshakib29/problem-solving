# https://www.hackerrank.com/challenges/plus-minus/problem

ara = []
pos = 0
neg = 0
zer = 0

n = int(input())
ara = list(map(int, input().split()))

for i in range(n):
    if ara[i] == 0:
        zer = zer + 1
    elif ara[i] < 0:
        neg = neg + 1
    else:
        pos = pos + 1
        
print(str(pos/n))
print(str(neg/n))
print(str(zer/n))