n = int(input())
for i in range(n):
    words = str(input())
    
    characters = [i for i in words]

    len_cha = len(characters)

    if len_cha <= 10:
        print(words)
    else :
        print(characters[0] + str(len(characters[1:-1])) + characters[-1])