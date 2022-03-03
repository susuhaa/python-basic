absent = [2,5] # 결석
no_book = [7] # 책을 잊어버렸다.
for student in range(1,11): # 1~10
    if student in absent:
        continue # 다음 반복 계속 진행

    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break # break를 만나면, 반복문 끝난다.
    print("{0}, 책을 읽어봐".format(student))

# 출석 번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)