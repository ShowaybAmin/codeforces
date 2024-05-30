s = input()

letters = [i for i in s]

upper = []
lower = []

for x in range (len(letters)) :
    if letters[x].isupper() == True :
        upper.append(letters[x])
    else:
        lower.append(letters[x])

if len(upper) > len(lower):
    print(s.upper())
else :
    print(s.lower())