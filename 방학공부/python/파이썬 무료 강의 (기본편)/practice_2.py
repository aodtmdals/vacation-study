# 2-1 (연산자)
from random import *
from math import *

a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a ** b)  # a^b
print(a % b)  # a/b의 나머지
print(a // b)  # a/b의 몫

print(10 > 3)
print(4 >= 7)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

# not
print(1 != 3)
print(not(1 != 3))

# and
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

# or
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(3 > 4 > 7)
print(8 > 5 > 1)


# 2-2 (간단한 수식)
# 파이썬은 괄호, 우선순위 연산 모두 알아서 해줌


number = 2 + 4 * 8
print(number)

# (number = number + 2) == (number += 2) 다른 계산부호도 같은 문법
number = number + 2
print(number)
number += 2
print(number)


# 2-3 숫자처리함수
# 절대값
print(abs(-5))
# 제곱
print(pow(4, 2))
# 최대값
print(max(1, 2, 3, 8))
# 최소값
print(min(1, 2, 3, 8))
# 반올림
print(round(3.14))
print(round(5.97))

# math 라이브러리 사용
# 내림
print(floor(4.99))
# 올림
print(ceil(3.14))
# 제곱근
print(sqrt(16))


# 2-4 (랜덤함수)
# 랜덤함수로 난수 뽑기
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
