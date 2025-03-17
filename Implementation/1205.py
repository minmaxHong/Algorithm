import sys

N, A, P = map(int, input().split())
if N == 0:
    print(1)
    sys.exit()

score_list = [-1] * P
scores = list(map(int, input().split()))[:N]
last_score = scores[-1]

# 일단은 입력을 다 받기
for i in range(N):
    score_list[i] = scores[i]

# 현재 
if N == P and A <= last_score:
    print(-1)
    sys.exit()

elif N == P and A > last_score:
    if last_score < A:
        score_list[-1] = A
    score_list = sorted(score_list, reverse=True)

    rank = 0
    for i in range(P):
        if score_list[i] >= 0:
            rank += 1
            if score_list[i] == A:
                print(rank)
                break

elif N < P:
    score_list[N] = A
    score_list = sorted(score_list, reverse=True)
    rank = 0
    for i in range(P):
        if score_list[i] >= 0:
            rank += 1
            if score_list[i] == A:
                print(rank)
                break