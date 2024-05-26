n, k = map(int, input().split())

score = list(map(int, input().split()))

participants = len([i for i in score if i >= score[k - 1] and i != 0])

print(participants)
