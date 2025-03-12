import sys
n = int(sys.stdin.readline())

words = []

for i in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)
words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)