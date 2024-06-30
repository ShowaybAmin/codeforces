n = int(input())
x = 0

for i in range (n):
    operation = str(input())
    operands = [a for a in operation]
    if '+' in operands:
        x += 1
    else:
        x -= 1
print (x)
