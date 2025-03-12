import sys

numbers = []
num = int(sys.stdin.readline())
for _ in range(num):
    x,y = map(int,sys.stdin.readline().split())
    numbers.append((int(x),int(y)))
numbers.sort() # x축 기준으로 자동으로 정렬 된다. -> x가 같으면 y를 자동으로 오름차순 정렬

for x,y in numbers:
    print(x,y)
    
### 푸는 방식

# 일단 중요한거 sort가 중요함 왜냐하면 sort는 우선적으로 튜플에서 x축기준으로 정렬을 진행함. 근데 x축이 같다면 y축을 기준으로 오름차순 정렬을 자동으로 해준다. 

# 나머지는 쉬워서 생략    