import sys
n = int(input())
stack = []

for i in range(n):
    command = sys.stdin.readline().split() # split을 이용해서 command[0] 과 [1]을 구별해서 문제를 푼다 

    if command[0] == "push":
        stack.append(int(command[1])) 
    elif command[0] == "pop":
        print(stack.pop() if stack else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(0 if stack else 1)
    elif command[0] == "top":
        print(stack[-1] if stack else -1) #이건 stack [-1] 써서 가장 최상단에 있는 숫자를 가져온다. 
