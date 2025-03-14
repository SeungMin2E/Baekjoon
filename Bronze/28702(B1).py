# 3의배수이면 Fizz 출력
# 5의 배수이면 Buzz 출력
# 3,5배수이면 FizzBuzz 출력
import sys

for i in range(0,3):
    x = sys.stdin.readline().strip() #개행 문자 제거(개행문자는 \n과 같은걸 말함 내가 엔터누르면 문자열상 \n가 자동으로 들어가서 필요함)
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x)+3-i # 여기가 중요 
if n%15==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)


