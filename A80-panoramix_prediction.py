n, m = map(int,input().split())

def prime(x):
    for i in range (2, ((x//2)+1)):
        if (x % i) == 0:
            break
    else:
        return True

for i in range ((n+1), (m+1)):
    if (prime(i) == True) and (i != m):
        print ("NO")
        break
    elif (prime(i) == True) and (i == m):
        print ("YES")
    else:
        print ("NO")
