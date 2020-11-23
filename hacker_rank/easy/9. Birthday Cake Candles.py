candle = []
no = 1

n = int(input())
candle = list(map(int, input().split()))

candle.sort(reverse=True)

max = candle[0]

for i in range(1, n):
    if candle[i] == max:
        no = no + 1
    else:
        break
        
print(str(no))
