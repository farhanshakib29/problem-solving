apple = []
orange = []
a_no = 0
o_no = 0

s, t = map(int, input().split()) #range of house
a, b = map(int, input().split()) #position of trees
m, n = map(int, input().split()) #no of fruits

apple = list(map(int, input().split())) #apple dist. from apple tree
orange = list(map(int, input().split())) #orange dist. from orange tree

for i in range(m):
    apple[i] = apple[i] + a
    if (apple[i]>=s) and (apple[i]<=t):
        a_no = a_no + 1

for i in range(n):
    orange[i] = orange[i] + b
    if (orange[i]>=s) and (orange[i]<=t):
        o_no = o_no + 1

print(str(a_no))
print(str(o_no))

