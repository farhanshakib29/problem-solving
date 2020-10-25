# https://www.hackerrank.com/challenges/staircase/problem

n = int(input())
for i in range(1, n+1):
    # print n-i spaces and i #s
    print(' '*(n-i) + '#'*i)