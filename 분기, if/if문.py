# weather ="미세먼지"
weather = input("오늘 날씨는 어때요? ")

if weather =="비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어떄요? ")) # 항상 숫자로 받기 때문에 int로 감싸준다.
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0<= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


