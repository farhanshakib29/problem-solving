n, k = map(int, input().split())
bills = list(map(int, input().split()))
bill_c = int(input())
sum = 0

for i in range(n):
    sum = sum + bills[i]
sum = sum - bills[k]

x = int(bill_c - sum/2)

if x==0:
    print('Bon Appetit')
else:
    print(str(x))
