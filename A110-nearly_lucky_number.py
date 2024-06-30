n = input()
flag = False
digit = 0

for _ in range (len(n)):
    if n[_] in ['4', '7']:
        digit += 1

if digit == 4 or digit == 7:
    flag = True

if flag :
    print("YES")
else:
    print("NO")