# 해싱(Hashing)은 어떤 데이터를 고정된 크기의 숫자(해시 값, Hash Value)로 변환하는 과정
# 문자열을 숫자

import sys

L = int(sys.stdin.readline())
name = sys.stdin.readline().strip()
r = 31
M = 1234567891

sum = 0
power = 1
# 아스키코드로 a~z까지 숫자로 변환해주고 
# 숫자값 = ord(문자) - ord('a') + 1 
#  abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.
for i in range(L):
    num = ord(name[i]) - ord('a')+1
    sum = (sum + num * power) % M  # mod M 적용
    power = (power * r) % M # 다음 r^i 값을 계산 (mod M 적용)
# 원래 내가 하던대로 하면 sum이 오버플로우 발생해서 너무 값이 커짐
# 그래서 mod M을 적용해야함 
print(sum)