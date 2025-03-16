# 피갤컵 A번 문제
year =2024
month = 8

num = int(input())
   
if num == 1:
    print(year,month)
elif num == 2:
    month+=7
    if month >=13:
        year+=1
        month-=12
    print(year,month)
elif num == 3:
    month+=2
    year+=1
    print(year,month)
elif num == 4:
    month-=3
    year+=2
    print(year,month)
elif num == 5:
    month+=4
    year+=2
    print(year,month)
