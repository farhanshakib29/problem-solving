# https://www.hackerrank.com/challenges/compare-the-triplets/problem

n = 3
alice = []
bob = []

alice[0:n] = map(int, input().split())
bob[0:n] = map(int, input().split())

alice_p = 0
bob_p = 0

for i in range(n):
    if alice[i] > bob[i]:
        alice_p += 1
    elif alice[i] < bob[i]:
        bob_p += 1
    else:
        continue

print(alice_p, bob_p)