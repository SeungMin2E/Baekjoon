num = int(input())
numbers = []
for _ in range(num):
    amusu = int(input())
    if amusu == 0:
        if numbers:
            numbers.pop()
    else:
        numbers.append(amusu)
print(sum(numbers))

### 푸는 방식
#일단 몇개입력받을지 정하고 난 후에 for문을 돌려서 반복해주고 amusu(아무수) 입력을 받은 다음에 amusu에 0이 들어갈때마다 배열에서 제일 최근에 넣은게 하나씩 빠져나와야하니까 스택 개념!!!!
#그러면 pop을 이용해준다. 그리고 0이 아닌 다른 수들은 배열에 그대로 채워주는 용도로 append써주고 마지막에 sum 으로 다 합해준다!