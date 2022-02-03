# 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
# 1-1 (숫자 자료형)
print(5)
print(-10)
print(3.14)
print(10000)
print(5+3)
print(2*8)
print(3*3+4)

# 1-2 (문자 자료형)
print('풍선')
print("나비")
print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
print('z'*9)  # 문자 자료형과 숫자 자료형 조합 가능

# 1-3 boolean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5 > 10))

# 1-4 변수
# 1. 변수 사용 X
print("우리 집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이고, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")


# 2. 변수 사용 O
animal = "강아지"
name = "백곰이"
age = 2  # 정수형은 문자열로 형변환
hobby = "터그놀이"
is_adult = age >= 3  # 불리안도 문자열로 변환

print("우리 집" + animal + "의 이름은 " + name + "에요")
print(name + "는" + str(age) + "살이고, " + hobby + "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# 2-1. 변수 사용 O (+대신 , 넣어보기)
animal = "강아지"
name = "백곰이"
age = 2  # 정수형은 문자열로 형변환
hobby = "터그놀이"
is_adult = age >= 3  # 불리안도 문자열로 변환

print("우리 집", animal, "의 이름은 ", name, "에요")
print(name, "는", str(age), "살이고, ", hobby, "를 아주 좋아해요")
print(name, "는 어른일까요? ", str(is_adult))


# 1-5 주석
# 는 주석
'''는 여러 문장을 주석처리하고 싶을 때 사용'''
