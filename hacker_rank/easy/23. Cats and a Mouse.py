n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())
    pos_a = abs(z-x)
    pos_b = abs(z-y)

    if pos_a < pos_b:
         print('Cat A')
    elif pos_a > pos_b:
         print('Cat B')
    else:
        print('Mouse C')
