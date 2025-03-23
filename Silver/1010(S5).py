# 다리놓기 
# 조합 문제 공식 이용 ! 
# N=13, M=29 
import math
import sys

a = int(sys.stdin.readline().strip())  # 테스트 케이스 개수 입력

for _ in range(a):
    N, M = map(int, sys.stdin.readline().strip().split())
    
    # 올바른 조합 공식 적용
    king = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    
    print(king)  # 각 테스트 케이스 결과 출력
# 이거 조합 공식 모르면 못품... ㅋㅋ;; gpt 물어봐서 알게됨.. 
# 이거 그냥 단순히 조합 공식 이용하는거 같음 