import math

num = int(input())
factorial_result = str(math.factorial(num))

count = 0
for a in reversed(factorial_result):
    if a =='0':
        count+=1
    else:
        break

print(count)

# ### 푸는 방식
# 일단 팩토리얼의 0의 개수를 찾는거니까 일단 factorial 함수를 쓰기위해서 math 함수를 이용해줬음 그리고 팩토리얼로 변한 값을 str (문자열) 로 변환을 해준다. 그렇게 했을 때 문자열이니까 문자를 기준으로 0의 개수를 샐 수 있다. 
# 그리고 0의 개수만 새면 되니까 for a in reversed(factorial_result) 하면 팩토리얼의 수를 뒤집어 주는거고 0이 나오면 카운트의 수를 1  증가시켜준다 그 외에는 전부 break를 걸어준다. 그리고 마지막에 카운트 수를 출력