Y, W = map(int, input().split())

if Y > W :
    x = Y 
else :
    x = W

A = 6 - (x -1)
i = 6
while i>0:
    if (6 % i == 0) and (A % i == 0):
        A = A // i
        break
    else:
        i = i - 1

print(f"{A}/{6//i}")
