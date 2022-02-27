
# quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자중 처음 세자리 + 글자갯수 + 글자내 "e" 갯수 + "!"로 구성

# 생성된 비밀번호

password = "http://naver.com"
my_str = password.replace("http://"," ") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
# my_str[0:5] -> 0~5 직전까지 (0,1,2,3,4)
# print(my_str)

passw = my_str[:4] + str(len(my_str))+ str(my_str.count("e"))+"!"
print('{0}의 비밀번호는{1} 입니다.' .format(password,passw))