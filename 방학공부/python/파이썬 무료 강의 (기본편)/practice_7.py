# 7-1. 표준 입출력
import pickle
import pickle
import sys

# sep defalut = " ", end defalut = "\n"
print("python", "Java", sep=",", end="?")
print("무엇이 더 재미있을까요?")


print("python", "Java", file=sys.stdout)  # 표준출력
print("python", "Java", file=sys.stderr)  # 표준에러 (따로 에러처리 가능)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))


# 7-2. 다양한 출력포맷
# 빈자리는 빈공간, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 땐 +, 음수일 때는 -표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽정렬, 빈칸은 _로 채움
print("{0:_<10}".format(500))

# 세 자리마다 콤마 찍어주기
print("{0:,}".format(500000000000))

# 세 자리마다 콤마 찍어주기 +,- 부호도 붙이기
print("{0:+,}".format(500000000000))

# 세 자리마다 콤마 찍어주기 +,- 부호도 붙이고 자릿수도 확보
# 빈자리는 ^로 채움
print("{0:^<+30,}".format(500000000000))


# 7-3. 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 추가로 쓰기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")

lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()


# 7-4. pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


# 7-5. with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
