n = int(input())
group_word_count = 0  

for i in range(n):
    word = input()  # 단어 입력 받고
    seen = set()  # seen이라는 변수에 set()이라는 중복없이 들어가게 만들어주고 
    previous_char = ''  # 이것도 previous_char 이라는 변수에 문자로 들어갈수 있게 만들어주고 
    is_group_word = True  # 처음엔 모두 그룹 단어라고 가정

    for char in word: 
        if char != previous_char:
            if char in seen:
                is_group_word = False  # 그룹 단어가 아님을 명확히 표시
                break  
            seen.add(char) # char에 새로운 단어가 들어오면 seen에 추가해주는 용도 
        previous_char = char  # 계속 업데이트 시켜주는 용도 

    if is_group_word:  # 그룹 단어일 경우에만 증가
        group_word_count += 1  

print(group_word_count)
