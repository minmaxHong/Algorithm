info = input().split()
player, game = int(info[0]), info[1]

friends = set()
for _ in range(player):
    friends.add(input())

friends = list(friends)

if game == 'Y':
    print(len(friends))
elif game == 'F':
    print(len(friends) // 2)

elif game == 'O':
    print(len(friends) // 3)