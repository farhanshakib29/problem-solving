#https://www.hackerrank.com/challenges/3d-surface-area/problem
"""
input the matrix
at the same time get maximum value
and total max value count
because, that is the total plane at top
and also add padding
"""
r, c = map(int, input().split())
m = []
mx = 0
mx_count = 0

for i in range(r):
    row = list(map(int, input().split()))
    _mx = max(row)
    if _mx == mx:
        mx_count += len([i for i, j in enumerate(row) if j == mx])
    elif _mx > mx:
        mx = _mx
        mx_count = len([i for i, j in enumerate(row) if j == mx])
    
    # add left and right padding
    row = [0] + row + [0]
    m.append(row)

# add top, bottom padding
pad = [0 for i in range(c+2)]
m.insert(0, pad)
m.append(pad)

"""
getting bottom plane number is easy
multiply row and column.
add it with top plane.
"""
plane = r*c + mx_count

"""
now, start from top level. calculate side planes for each block.
each block has a side plane, if the value is less than current level.
do same for left, right, front, back.
at the same time, calculate top plane of next level.
next plane has a top plane if the value is equal to (current level-1)
"""
for i in range(mx, 0, -1):
    for j in range(1, r+1):
        for k in range(1, c+1):
            if m[j][k] == i-1:
                plane += 1
            elif m[j][k] == i:
                if m[j][k-1] < i:
                    plane += 1
                if m[j][k+1] < i:
                    plane += 1
                if m[j-1][k] < i:
                    plane += 1
                if m[j+1][k] < i:
                    plane += 1

    for p in range(1, r+1):
        for q in range(1, c+1):
            if m[p][q] == i:
                m[p][q] -= 1 

print(plane)

