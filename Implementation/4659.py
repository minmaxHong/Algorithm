must = ['a', 'e', 'i', 'o', 'u'] # 모음음

while True:
    sence = input()
    if sence == "end":
        break

    first_flag = False
    second_flag = True
    third_flag = True

    word_num = 0
    vowel_num = 0 # 모음
    consonant_num = 0 # 자음음
    same_num = 0
    for word in sence:
        if word in must and word_num == 0:
            word_num += 1
            first_flag = True
            break
        
    for word in sence:
        if word in must:
            vowel_num += 1
            consonant_num = 0
        else:
            consonant_num += 1
            vowel_num = 0
        
        if vowel_num == 3 and consonant_num == 0:
            second_flag = False
            break
        elif vowel_num == 0 and consonant_num == 3:
            second_flag = False
            break
    
    compare_word = sence[0]
    for i in range(1, len(sence)):
        if compare_word == 'e' or compare_word == 'o':
            compare_word = sence[i]
        elif compare_word == sence[i]:
            third_flag = False
            break
        else:
            compare_word = sence[i]
            third_flag = True

    if first_flag and second_flag and third_flag:
        print(f"<{sence}> is acceptable.")
    else:
        print(f"<{sence}> is not acceptable.")