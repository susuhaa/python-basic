# 단어가 있는 뜻 처럼, 키와 해당하는 사전이 있다, 중복이 안된다.

cabinet = {3:"유재석",100:"김태호"} #사전의 경우 중괄호로 키와 벨류를 넣는다.
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#대괄호로 가져올떄는 값이 없을경우 오류를 출력하고 멈춘다
# 소괄호로 가져올떄는 none이라고 띄우고 계속 출력한다.
# 만약 없는 값을 가져올떄 기본값을 쓰고싶다면
print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))

print(3 in cabinet) # 3이라는 키가 있다면 true가 나온다.

cabinet = {"A-3": "유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"]="김종국" # 기존 키 유재석위에 김종국이 덮어써진다.
cabinet["C-20"]= "조세호"

print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)




