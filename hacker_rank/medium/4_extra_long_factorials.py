# https://www.hackerrank.com/challenges/extra-long-factorials/problem

def long_factorial(num):
    fact = 1
    i = 1
    while i <= num:
        fact = fact * i
        i += 1
    return fact

num = int(input()) 
print(long_factorial(num))