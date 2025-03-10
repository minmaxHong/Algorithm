N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]

head_y, head_x = 0, 0
heart_y, heart_x = 0, 0
left_arm, right_arm, back, left_leg, right_leg = 0, 0, 0, 0, 0

head_flag = False
for y in range(N):
    for x in range(N):
        if arr[y][x] == "*":
            heart_y = y + 1
            heart_x = x
            head_flag = True
            break
    if head_flag:
        for x in range(heart_x): # 왼 팔
            if arr[heart_y][x] == "*":
                left_arm += 1
        for x in range(heart_x+1, N): # 오른 팔
            if arr[heart_y][x] == "*":
                right_arm += 1
        for y in range(heart_y+1, N):
            if arr[y][heart_x] == "*":
                back += 1
        for y in range(heart_y+1, N):
            if arr[y][heart_x-1] == "*":
                left_leg += 1
        for y in range(heart_y+1, N):
            if arr[y][heart_x+1] == "*":
                right_leg += 1

        break

print(heart_y+1, heart_x+1)
print(left_arm, right_arm, back, left_leg, right_leg)