# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# https://stackoverflow.com/questions/1622532/algorithm-to-find-next-greater-permutation-of-a-given-string

def swap(word, i, j):
    temp = word[i]
    word[i] = word[j]
    word[j] = temp

def next_bigger():
    data = list(input())
    k = 0 
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            k = i

    l = 0
    for i in range(k+1, len(data)):
        if data[i] > data[k]:
            l = i

    if k==l:
        print('no answer')
        return
    
    swap(data, k, l)
    data = data[0:k+1] + data[len(data)-1:k:-1]
    print(''.join(data))

for i in range(int(input())):
    next_bigger()