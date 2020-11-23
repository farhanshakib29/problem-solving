n = int(input())
a = list(map(int, input().split()))
a.sort()
max_l = 0

for i in range(n):
    b = []
    for j in range(i, n):
        if abs(a[j]-a[i]) <= 1:
            b.append(a[j])

    if len(b) > max_l:
        max_l = len(b)

print(str(max_l))
