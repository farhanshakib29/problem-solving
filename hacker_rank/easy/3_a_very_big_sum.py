# https://www.hackerrank.com/challenges/a-very-big-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = int(input())
nums = []
nums[0:n] = map(int, input().split())

sum = 0
for num in nums:
    sum += num

print(sum)