Dial = {'A':3,'B':3,'C':3,'D':4,'E':4,'F':4,'G':5,'H':5,'I':5
        ,'J':6,'K':6,'L':6,'M':7,'N':7,'O':7,'P':8,'Q':8,'R':8,'S':8
        ,'T':9,'U':9,'V':9,'W':10,'X':10,'Y':10,'Z':10}
# 딕셔너리 써주고 
n = input() # 입력한거 그대로 더해버리면 값이 안나오니까 
total_time = 0 
for char in n: # for문으로 입력한 문자 하나하나 들어가게 해준다음 
    total_time += Dial[char] # 먼저 W들어가니까 10+0 하고 그다음 10에 A더해주면 
print(total_time) #13이 나옴
