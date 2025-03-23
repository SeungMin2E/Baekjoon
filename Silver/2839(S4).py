# 설탕 배달 
# 최소한으로 적은 봉지를 들고 가야함 ! 
# 18 키로를 3이랑 5로 나눠야함 
# 3키로랑 5키로가 기준 ! 
# 3이랑 5로 못나누면 -1 출력
import sys
kg = int(sys.stdin.readline())

Xbongtu = kg // 5 # 이건 X라는 변수에 내가 입력한 kg을 5로 나눠줌 
# 이렇게 해서 최대한 5키로로 몫을 구해서 최대한의 5키로 개수를 만드는거지

while Xbongtu >= 0: # 일단 Xbongtu가 0이상일때엔 계속 while문 돌아가게 하고 
    remain = kg - (5 * Xbongtu) # remain이라는 변수 만들어서 남는 kg 만들어주고 
    if remain % 3 == 0 : # 여기서 남은걸 3키로로 나눴을때 나머지가 0이면 ybongtu 개수를 세준다
        Ybongtu = remain//3
        print(Xbongtu + Ybongtu) # 둘이 합친거
        break
    Xbongtu -=1 # 만약 11kg과 같이 5키로 2개썻을때 나머지가 1인경우 xbongtu 값을 줄여줘서 다시 while문을 실행하게 한다음 계산! 
else:
    print(-1)
    