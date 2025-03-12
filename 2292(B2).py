import sys

n = int(sys.stdin.readline())

layer =  1
num = 1

while num<n:
    num+=6*layer
    layer+=1

print(layer)