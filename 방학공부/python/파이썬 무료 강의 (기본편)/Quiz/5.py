'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해짐
조건 2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야합니다.

(출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
...
[] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

from random import *
count = 0
for i in range(50):
    time = randint(5, 51)
    if time >= 5 and time <= 15:
        count += 1
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))
    print("[] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))
print("\n총 탑승 승객 : {0}분".format(count))
