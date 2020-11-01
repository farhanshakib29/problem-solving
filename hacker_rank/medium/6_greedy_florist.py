# https://www.hackerrank.com/challenges/greedy-florist/problem

import math

# we have n flowers, k people, n>=k
# ex- n=5, k=3, costs=1,3,5,7,9
# we construct a matrix like form, with costs reversed grouped with k=3
# because, high costs flowers will be bought less, and low costs will be bought more
#
# 9 7 5
# 3 1 x
#
# top row will be bought 1 times, next row 2 times and so on
# then -
# [9 7 5] x 1 + [3 1] x 2 = minimum cost

def minimize(n, k, cost):
    rest = n
    price = 0
    for row in range(math.ceil(n/k)):
        rest -= k
        start = row * k

        if rest > 0:
            end = start + k
        else:
            end = n

        for col in range(start, end):
            price += (row + 1) * cost[col]
    
    return price

n, k = map(int, input().split())
cost = list(map(int, input().split()))
cost.sort(reverse=True)
print(minimize(n, k, cost))