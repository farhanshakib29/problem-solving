n = int(input())
socks = list(map(int, input().split()))
socks.sort()
pairs = 0

i = 0
while True:
    if i >= n-1:
        break
    elif socks[i] == socks[i+1]:
        pairs += 1
        i += 1
    i += 1

print(str(pairs))
