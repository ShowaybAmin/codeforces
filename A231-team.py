n = int(input())

result = 0

for i in range (n) :
    x, y, z = map(int, input().split())
    if (x + y + z) > 2 :
        result += 1
print(result)
