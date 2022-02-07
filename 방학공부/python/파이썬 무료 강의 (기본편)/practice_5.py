# if
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요.")


# for
for waitiong_no in range(1, 6):
    print("대기번호 : {0}".format(waitiong_no))

starbucks = ["아이언맨", "토르", "구르트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while
coffee_customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(coffee_customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

person = "Unknown"
while person != coffee_customer:
    print("{0}, 커피가 준비되었습니다".format(coffee_customer))
    person = input("이름이 어떻게 되세요? ")


# continue and break
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책 읽어봐".format(student))


# 한 줄 for
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)
