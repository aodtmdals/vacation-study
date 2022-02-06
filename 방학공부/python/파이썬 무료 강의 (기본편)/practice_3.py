from unittest.mock import sentinel


# 3-1. 문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)


sentence3 = """
    나는 소년이고,
    파이썬은 쉬워요.
"""
print(sentence3)


# 3-2 슬라이싱
jumin = "001212-4XXXXXX"
print("성별 : " + jumin[7])
print("년 : " + jumin[0:2])  # 0~2직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("주민등록 뒷자리 : " + jumin[7:])
print("주민등록 뒷자리(뒤부터) : " + jumin[-7:])


# 3-3 문자열처리함수
python = "python is Amazing"
print(python.lower())  # 소문자로 출력
print(python.upper())  # 대문자로 출력
print(python[0].isupper())
print(len(python))
print(python.replace("python", "java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("n"))
print(python.find("java"))
# print(python.index("java"))

print(python.count("n"))


# 3-4 문자열 포맷
print("나는 20살입니다")

# 방법 1
print("나는 %d살입니다" % 20)
print("나는 %s를 좋아해요" % "python")
print("Apple은 %c로 시작해요" % 'A')

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4 (v3.6이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요.")


# 3-5 탈출문자
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

print("저는 \"나도코딩\" 입니다")
print("\\^▽ ^ 안녕")
print("red apple\rpine")

print("redd\bapple")

print("Red\tApple")
