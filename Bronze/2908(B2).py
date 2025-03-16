# 숫자를 거꾸로 읽어라 
num = list(map(str,input().split()))
nums = []

reverse_numb = num[0][::-1] #슬라이싱!! ::1은 뒤에서부터 출력 [0]인 이유는 앞에거 출력
revers_num = num[1][::-1]

nums.append(int(revers_num))
nums.append(int(reverse_numb))

print(max(nums))