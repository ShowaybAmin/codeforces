n = int(input())
s = input()

i = 0

for _ in range(n - 1):
    if s[_] == s[_ + 1]:
        i += 1

print(i)