from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님
        print("[0] {0}번째 손님(소요시간 : {1}분".format(i,time))