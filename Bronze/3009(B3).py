x_list = [] # 리스트 2개 만들어주고 각각 만들어주는건 
y_list = [] # 규칙이 x가 5 5 7 이면 7이 한개 더필요해서 
for i in range(3):
    A,B = map(int,input().split())
    x_list.append(A)
    y_list.append(B)

for i in x_list:
    if x_list.count(i) == 1: # x리스트에서 i의 수를 세는데 그 중에서 1개인거 출력해주고 
        x4 = i
for j in y_list:
    if y_list.count(j) == 1:
        y4 = j
print(x4,y4)