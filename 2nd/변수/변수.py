# 애완동물을 소개해 주세요~
animal = "고양이"
name = "연탄이"
age = 4 # 정수형 자료이기 때문에 따옴표 없이 씀
hobby = "산책"
is_adult = age>= 3


# 이름이 해피로 달라졌을 경우
print("우리집 " + animal + "의 이름은 " + name +"에요")
hobby = "공놀이" #변수는 중간에 덮어 쓸수 있다.
print(name +"는" + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" +str(is_adult))


print("우리집 " + animal + "의 이름은 " + name +"에요")
hobby = "공놀이" #변수는 중간에 덮어 쓸수 있다.
print(name,"는" ,age, "살이며," ,hobby, "을 아주 좋아해요")
print(name + "는 어른일까요?" +str(is_adult))

