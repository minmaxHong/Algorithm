import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    flag = False
    user_input = input().strip()
    if user_input == 'all':
        S = set(range(1, 21))
        flag = True
    elif user_input == 'empty':
        S = set()
        flag = True
    
    if not flag:
        oper, find_s = user_input.split(" ")
        find_s = int(find_s)
        if oper == 'add':
            S.add(find_s)

        elif oper == 'check':
            print(1 if find_s in S else 0)
            
        elif oper == 'toggle':
            if find_s in S:
                S.discard(find_s)
            else:
                S.add(find_s)

        elif oper == 'remove':
            if find_s in S:
                S.discard(find_s)