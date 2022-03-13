
absent = [2,5] # 결석
no_book = [7] # 책을 안가져온 학생
for student in range(1,11): 
    if student in absent:
        continue # 건너띄고 계속 진행
    elif student in no_book:
        print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
        break # 멈춤
    print("{0}, 책을 읽어봐".format(student))


# 한줄로 끝내는 for문
# 출석번호가 1,2,3,4 앞에 붙이기로함 -> 101, 102, 103

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


