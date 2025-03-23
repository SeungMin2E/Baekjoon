n = int(input())  # 사용자로부터 입력을 받아 정수로 변환
line = 1          # 몇 번째 대각선인지 나타내는 변수

while n > line:   # n이 현재 대각선(line)의 개수보다 크면 반복
    n -= line     # 현재 대각선에 있는 숫자 개수(line)만큼 n에서 빼줌
    line += 1     # 다음 대각선으로 이동
# 여기서 n=4이면 line=3이되고 n=1이 남는데 이때 3라인의 1번째 분수가 답이된다

# 짝수 계산 
if line % 2==0:
    a = n #여기 n은 위에서 while문 돌리고 남은 n이 여기로 내려와서 진행
    b = line - n + 1 # 여기도 위에 while문 돌리고 남은 line이랑 n으로 풀기 
# 홀수 계산
elif line %2 == 1:
    a = line - n +1 
    b = n

print(f'{a}/{b}')