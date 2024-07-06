n = int(input())

p = map(int, input().split())

total = 0

for i in p :
    total = total + i

print(total / n)