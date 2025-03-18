switch_num = int(input())
switch_status = [-1] + list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    sex, index = map(int, input().split())

    # man
    if sex == 1:
        for j in range(index, len(switch_status), index):
            if switch_status[j] == 0:
                switch_status[j] = 1
            elif switch_status[j] == 1:
                switch_status[j] = 0
    # woman
    elif sex == 2:
        if switch_status[index] == 0:
            switch_status[index] = 1
        elif switch_status[index] == 1:
            switch_status[index] = 0
        
        start_index, end_index = 2, 2
        if start_index >= 2:
            start_index = index - 1
        if end_index <= len(switch_status) - 1:
            end_index = index + 1

        while start_index >= 1 and end_index < len(switch_status):
            if switch_status[start_index] == switch_status[end_index]:
                if switch_status[start_index] == 0:
                    switch_status[start_index] = 1
                    switch_status[end_index] = 1
                elif switch_status[start_index] == 1:
                    switch_status[start_index] = 0
                    switch_status[end_index] = 0

                start_index -= 1
                end_index += 1
            else:
                break

for i in range(1, len(switch_status)):
    print(switch_status[i], end = " ")
    if i % 20 == 0:
        print()