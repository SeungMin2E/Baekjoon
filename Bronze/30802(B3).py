import sys

N=int(sys.stdin.readline().strip())
Sizes = list(map(int,sys.stdin.readline().split()))
T,P = map(int,sys.stdin.readline().split())

Total_size = sum(Sizes)

Shirt = Total_size
if Shirt % T == 0:
    print(Shirt//T)
elif Shirt % T !=0:
    print(Shirt//T+1)

pen_bundle = N//P
remain_pen = N % P

print(pen_bundle,remain_pen)