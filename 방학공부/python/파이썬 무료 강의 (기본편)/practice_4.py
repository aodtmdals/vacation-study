# 리스트 [] 다양한 자료형을 넣을 수 있음

from tkinter import Menu


subway = [10, 20, 30]
print(subway)

subway = ["박명수", "조세호", "유재석"]
print(subway)


# 조세호 씨는 몇 번째 칸?
print(subway.index("조세호"))

# 다음 역에서 하하 씨 탐
subway.append("하하")
print(subway)

# 정현돈 씨를  유재석 / 하하 사이에 태워봄
subway.insert(3, "정현돈")
print(subway)

# 지하철이 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()
subway.pop()
subway.pop()
print(subway)


# 정렬
num_list = [5, 1, 8, 3, 6]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)


# 사전 {}
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[100])
print(cabinet.get(3))
# 값이 없으면?
# print(cabinet[5])    : 에러 출력
print(cabinet.get(5))  # None 출력
print(cabinet.get(5, "사용가능"))  # 값이 있으면 출력, 없으면 "사용가능"으로 지정하고 출력

# 값이 있는지 없는지
print(3 in cabinet)
print(8 in cabinet)

# 추가
cabinet["A-8"] = "모모"
print(cabinet)

# 삭제
del cabinet[3]
print(cabinet)

# key값만 출력
print(cabinet.keys())

# value값만 출력
print(cabinet.values())

# 둘 다 출력
print(cabinet.items())


# 튜플 () 값 추가 불가
menu = ("돈가스", "치즈까스")
print(menu[0])
print(menu[1])


# 튜플로 변수 선언 쉽게 하기
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# 집합(set) {} 중복 허용 X
my_sets = {1, 2, 3, 3, 4}
print(my_sets)

java = {"유재석", "박명수", "양세형"}
python = set(["유재석", "박명수", ])

# 교집합 출력
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))


# 값 추가
python.add("김태호")
print(python)

# 제거
python.remove("유재석")
print(python)


# 자료구조 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
