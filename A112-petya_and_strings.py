word1 = input().lower()
word2 = input().lower()

letters1 = [i for i in word1]
letters2 = [i for i in word2]

sorted_list = []
sorted_list.append(letters1)
sorted_list.append(letters2)
sorted_list.sort()

if letters1 == letters2:
    print(0)
elif sorted_list[0] == letters1:
    print(-1)
elif sorted_list[0] == letters2:
    print(1)
