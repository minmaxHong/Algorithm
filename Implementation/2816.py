n = int(input())
channel = ''
KBS1_index = 0
KBS2_index = 0

for i in range(n):
    chn_name = input()
    if chn_name == 'KBS1':
        KBS1_index = i
    elif chn_name == 'KBS2':
        KBS2_index = i

channel += '1' * KBS1_index
channel += '4' * KBS1_index
if KBS1_index > KBS2_index:
    KBS2_index += 1
channel += '1' * KBS2_index
channel += '4' * (KBS2_index - 1)

print(channel)