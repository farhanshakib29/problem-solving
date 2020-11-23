b, n, m = input().split()
b = int(b)
n = int(n)
m = int(m)
key = list(map(int, input().split()))
usb = list(map(int, input().split()))
pri = []
price = -1

for i in range(n):
    for j in range(m):
        pri.append(key[i]+usb[j])

pri.sort(reverse=True)

for i in pri:
    if i <= b:
        price = i
        break

print(str(price))
