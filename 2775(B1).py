import sys

Testcase = int(sys.stdin.readline())

for _ in range(Testcase):
    K=int(sys.stdin.readline()) #층
    N=int(sys.stdin.readline()) # 호수

    aprt = [] #이걸로 0층 초기화 해주고 
    for i in range(1,N+1):
     aprt.append(i) # 어차피 1,2,3,4,5,6 이렇게 증가하니까 기본으로 이렇게 해줌
# apart = [[i for i in range(1,N+1)]] 컴프리헨션 사용

#1층부터 K층 채우기
    for floor in range(1,K+1):
        for room in range(1,N):
         aprt[room] = aprt[room]+aprt[room-1]
#aprt[1] = aprt[1] + aprt[0]
#3 = 2 + 1, 그럼 현재 상황 1층에 [1,3,3]
#그럼 aprt[2] = aprt[2] + aprt[1] 이면 3+3=6이됨
    print(aprt[-1])
#aprt[-1]은 리스트 마지막 원소 N-1써도 되긴함 
