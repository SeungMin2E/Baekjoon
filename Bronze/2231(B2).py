n = int(input()) # 숫자 입력 받고
result = 0 # 초기화 해주고
for i in range(1,n+1): # 여기는 1~내가 입력한 숫자까지 for문 돌려주고 
    nums = list(map(int,str(i))) # 여기가 중요한데 내가 입력한 숫자는 문자열이니까 그걸 정수로 하나씩 만들어서 리스트에 저장
    # 예를 들어 n=216이면 '2','1','6' 이 저장
    result = sum(nums) + i # 1+9+8+198
    if result == n: #result값이 n 내가 입력한 값이랑 같으면 출력
        print(i)
        break 

    if i == n: # 아니면 0출력력
        print(0)