#while 

customer = "토르"
index = 5
while index >= 1: # 조건이 만족할때까지 반복한다.
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1 # 인덱스를 한번씩 줄여나간다
    if index == 0: # 인덱스가 다 줄어들면 끝
        print("커피는 폐기 처분 되었습니다.")


# customer = "아이언맨"
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1 # 무한 루프

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
