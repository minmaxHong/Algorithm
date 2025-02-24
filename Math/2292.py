n = 1
target = int(input())
aws = 1

start_iter = 1
end_iter = 6
else_iter = 1
iter = 0
if target != 1:
    while True:
        start = n + start_iter
        end = n + end_iter

        if target >= start and target <= end:
            aws += iter
            break
            
        else:
            start_iter += (6 * else_iter)
            else_iter += 1
            end_iter += (6 * else_iter)
            iter += 1

    print(aws + 1)

else:
    print(aws)