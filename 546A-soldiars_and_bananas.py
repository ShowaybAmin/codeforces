k, n, w = map(int, input().split())
money = 0

for _ in range (w):
    money += (_ + 1) * k

print(money - n)