ar = []
pair = 0

n, k = map(int, input().split())
ar = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        sum = ar[i] + ar[j]
        if sum%k == 0:
            pair = pair + 1

print(str(pair))
