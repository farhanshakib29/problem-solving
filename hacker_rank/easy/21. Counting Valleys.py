n = int(input())
hike = input()
path = []
s = 0
valley = 0

for i in hike:
    if i=='U':
        s = s + 1
        path.append(s)
    else:
        s = s - 1
        path.append(s)

i = 0
while True:
    if i >= n:
        break
    elif path[i] == -1 and path[i+1] <= 0:
        for j in range(i+1, n):
            if path[j] == 0:
                valley = valley + 1
                i = j
                break
            j = j + 1
    i = i + 1

print(str(valley))
