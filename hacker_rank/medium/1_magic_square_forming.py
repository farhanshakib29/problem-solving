# https://www.hackerrank.com/challenges/magic-square-forming/problem

# input matrix list 
matrix = []
# keep cost
cost_l = []
# all combinations of magic square
magic = [
    [8,1,6,3,5,7,4,9,2],
    [8,3,4,1,5,9,6,7,2],
    [6,1,8,7,5,3,2,9,4],
    [4,3,8,9,5,1,2,7,6],
    [4,9,2,3,5,7,8,1,6],
    [6,7,2,1,5,9,8,3,4],
    [2,9,4,7,5,3,6,1,8],
    [2,7,6,9,5,1,4,3,8]
]

# input matrix as list of 9 elements
for i in range(3):
    matrix = matrix + list(map(int, input().split()))

# compare with magic squares and store cost
for i in range(8):
    cost = 0
    for j in range(9):
        cost += abs(matrix[j] - magic[i][j])
    cost_l.append(cost)

# sort cost and get the minimum one
cost_l.sort()
print(cost_l[0])