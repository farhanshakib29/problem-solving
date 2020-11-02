# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

n = int(input())
for i in range(n):
    bucket_no = int(input())

    # input buckets
    buckets = []
    buckets_len = []
    for j in range(bucket_no):
        new_bucket = list(map(int, input().split()))
        buckets.append(new_bucket)
        buckets_len.append(sum(new_bucket))

    # calculate no of balls of each color
    colors = [0 for i in range(bucket_no)]
    for bucket in buckets:
        for color in range(bucket_no):
            colors[color] += bucket[color]
    
    # the logic is- 
    # if we have 3 colors of balls with amount 4, 5, 3
    # we need buckets of size 4, 5, 3
    buckets_len.sort()
    colors.sort()

    if buckets_len == colors:
        print('Possible')
    else:
        print('Impossible')