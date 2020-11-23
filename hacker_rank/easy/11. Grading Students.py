def grade(ara, n):
    for i in range(n):
        if ara[i]<40:
            if ((ara[i]+1)==40) or ((ara[i]+2)==40):
                ara[i] = 40
        else:
            if (ara[i]+1)%5==0:
                ara[i] = ara[i] + 1
            elif (ara[i]+2)%5==0:
                ara[i] = ara[i] + 2
    
    for i in range(n):
        print(ara[i])


n = int(input())
ara = []

for i in range(n):
    ara.append(int(input()))

grade(ara, n)
