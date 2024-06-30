for _ in range (5):
    num = input().split(' ')
    if '1' in num:
        j = num.index('1') + 1
        i = _ + 1

print(abs(3 - i) + abs(3 - j))
