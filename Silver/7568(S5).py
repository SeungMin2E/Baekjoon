# 덩치 문제
# 규칙이 등수는 몸무게도 크고 키도 커야 덩치가 더 크다 
# 처음을 다 랭크를 1등으로 해줌 
# 그리고 각각 비교를 해서 큰 사람이 있으면 등수가 1 증가 

import sys
n = int(sys.stdin.readline())
inputs = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    inputs.append((a,b)) # 튜플로 넣고
# [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)] 현재 상황 
ranks = [] # ranks 리스트 하나 만들고 
for i in range(n):
    rank = 1 #전부를 랭크 1등으로 해주고 
    for j in range(n):
        if i != j: # 자기자신은 제외해주고 
            if inputs[i][0] < inputs[j][0] and inputs[i][1] < inputs[j][1]: #몸무게 랑 키 비교 해주고 
                rank +=1 # 덩치가 더크면 등수 증가 해주고 
    ranks.append(rank) # 랭크 넣어주고 
print(*ranks)