# 삼각형 외우기

triangle = [] 
for _ in range(3):
    A = int(input())
    triangle.append(A)

if sum(triangle) != 180: # 여기서 삼각형인지 아닌지 먼저 거르고
    print('Error')
elif triangle.count(60) == 3: 
    print('Equilateral')
elif len(set(triangle)) == 2:  # 두 변의 길이가 같다면 Isosceles
    print('Isosceles') # set을 써주고 len을 한건 set으로 일단 중복을 제거해주면 
elif len(set(triangle)) == 3:  # 세 변이 모두 다르다면 Scalene
    print('Scalene')
