# https://www.hackerrank.com/challenges/countingsort4/problem

data = []
n = int(input())

for i in range(int(n/2)):
    line = input()
    index = line.split()[0]
    data.append([int(index), '-'])

for i in range(int(n/2)):
    line = input()
    index, val = line.split()
    data.append([int(index), val])

data = sorted(data, key=(lambda x : x[0]))
sentence = [x[1] for x in data]
print(' '.join(sentence))