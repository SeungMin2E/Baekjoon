# 대칭 차집합 
# 구조는 첫줄에 A와 B의 개수를 입력해주고 
# 둘째줄은 A의 원소
# 셋째줄은 B의 원소
# 3 5
# 1 2 4
# 2 3 4 5 6
import sys
# 첫 번째 입력: a, b의 크기
a, b = map(int, input().split())

# 두 번째 입력부터 a개의 수: 집합 A의 원소들
A = set(map(int, sys.stdin.readline().split()))

# 그다음 입력부터 b개의 수: 집합 B의 원소들
B = set(map(int, sys.stdin.readline().split()))

print(len(A-B)+len(B-A))
print(A-B)

# 이거 라이트업 작성 해야함 !! 
