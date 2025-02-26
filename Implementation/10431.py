n = int(input())

arr = []
for _ in range(n):
    case = list(map(int, input().split()))
    testcase, stude = case[0], case[1:]

    aws = 0
    for i in range(1, len(stude)):  
        key = stude[i]  
        j = i - 1

        while j >= 0 and stude[j] > key:  
            stude[j + 1] = stude[j]
            j -= 1
            aws += 1  

        stude[j + 1] = key 

    arr.append(aws)

a = 0
for i in arr:
    a += 1
    print(f"{a} {i}")