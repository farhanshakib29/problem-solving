# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())
mat = []
a = []
pri = 0
sec = 0

for i in range(n):
    mat.append(list(map(int, input().split())))

for i in range(n):
   pri = pri + ara[i][i]

for i in range(n):
   sec = sec + ara[i][n-i-1]
    
print(str(abs(pri-sec)))