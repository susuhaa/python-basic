sentence = "나는 소년입니다"
print(sentence)

sentence2 ="파이썬은 쉬워요"

print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "999999-1234567" # 필요한 정보만큼 잘라서 사용
print("성별 : " + jumin[7])
print("연 : "+ jumin[0:2]) # 0 부터 2 직전까지(0,1)
print("월: "+ jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 :" + jumin[:6]) # 처음부터 6 직전까지
print("생년월일 :" + jumin[0:6]) # 처음부터 6 직전까지
print("뒤 7자리: " + jumin[7:]) # 7번째 부터 끝까지

print("뒤 7자리 (뒤에서 부터) :" +jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
# print(python.index("Java"))

print(python.count("n")) # 파이썬에서 n이 총 몇번 등장하는지

print("나는 %d 살입니다" %20)
print("나는 %s을 좋아해요" %"파이썬")
print("apple은 %c로 시작해요" %"A")

# %s
print("나는 %s살입니다" %20)
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

#방법 2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

#방법 4

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


