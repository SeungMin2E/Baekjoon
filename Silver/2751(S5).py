import sys
num = int(sys.stdin.readline())  # 입력 개수 받기
number = []

for i in range(num):
    numbers = int(sys.stdin.readline())  # 정수 입력 받기
    number.append(numbers)  # 리스트에 추가

# 리스트 정렬
number.sort()

# 출력
for n in number:
    print(n)
### 푸는 방식

# 일단 원래 수를 정렬하는 코드를 짜는 느낌으로 짜면 되는데 이게 시간초가 주어져있어서 import sys 에서 sys.stdin.readline()으로 시간을 단축해주고 

# num값 입력 받고 number=[] 로 리스트를 만들어줘서 sort를 할 수 있게 만들어준다 sort의 경우 리스트일때만 sort가 가능하기 떄문이다. 그렇게해서 number.sort() 해주고 마지막에 출력 해준다.