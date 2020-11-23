com = []

n = int(input())
ar = [0]*n
birds = list(map(int, input().split()))

for i in range(n):
    x = birds[i] - 1
    ar[x] = ar[x] + 1

max = 0

for i in range(n):
    if ar[i]>max:
        max = ar[i]

for i in range(n):
    if ar[i]==max:
        com.append(i+1)

l = len(com)
min = com[0]
for i in range(l):
    if com[i]<min:
        min = com[i]

print(str(min))
