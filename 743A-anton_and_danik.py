n = int(input())
s= input()

Anton = Danik = 0

for _ in range (n):
    if s[_] == "D":
        Danik += 1
    elif s[_] == "A":
        Anton += 1

if Anton == Danik:
    print("Friendship")
elif Anton > Danik:
    print("Anton")
else :
    print("Danik")