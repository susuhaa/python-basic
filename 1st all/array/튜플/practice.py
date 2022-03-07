#앞선 리스트들과는 다르게 중간에 추가가 불가능 하다.
#속도가 리스트보다 빠르다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 오류가 난다, 즉 리스트는 추가하거나 변경이 안된다.

name = "김종국"
age = 20
hobby = " 코딩 "
print(name, age, hobby)

(name, age, hobby) = ("김종국",20,"코딩")

print(name, age, hobby)


