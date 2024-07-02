n, h = map(int, input().split())
width = 0

friend_height = input().split()

for i in friend_height:
    if int(i) > h :
        width += 2
    else:
        width += 1
        
print(width)