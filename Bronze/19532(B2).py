# 수학은 비대면 강의다.
# 연립방정식 문제 
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

# 연립방정식 해 공식
x = (c * e - f * b) // (a * e - d * b)
y = (a * f - d * c) // (a * e - d * b)

print(x, y)
