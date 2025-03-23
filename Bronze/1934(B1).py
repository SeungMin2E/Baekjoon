import sys
import math

a = int(sys.stdin.readline().strip())

for i in range(a):
    A,B = map(int,sys.stdin.readline().strip().split())
    gcd_AB = math.gcd(A,B) # 최대공약수 구하는 공식
    A2 = A//gcd_AB # 최대공약수로 나눠주기 
    B2 = B//gcd_AB # 최대공약수로 나눠주기
    result = gcd_AB * A2 * B2
    print(result)