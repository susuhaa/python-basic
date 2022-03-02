# 리스트[]

#지하철 칸별로 10명 20명 20명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway=["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇번째 칸에 타고있는지
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 탄경우
subway.append("하하")   # 제일 뒤에 들어간다
print(subway)

# 정형돈씨를 유재석/ 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reserve()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함꼐 사용
mix_list= ["조세호", 20, True]
print(mix_list)

#리스트의 확장
num_list.extend()
print(num_list)


