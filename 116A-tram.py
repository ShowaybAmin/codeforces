n = int(input())
a = b = highest = total = 0


for i in range(n):
    a , b = map(int, input().split())

    total = (total - a) + b

    if total > highest :
        highest = total     

print(highest)