N, K = map(int, input().split())

arr = []
for i in range(N):
    info = list(map(int, input().split()))
    arr.append(info)

sorted_arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if sorted_arr[i][0] == K:
        idx = i 

for i in range(N):
    if sorted_arr[idx][1:] == sorted_arr[i][1:]:
        print(i+1)
        break