# 5. 함수
from cgi import print_directory


def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.(잔액부족)".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance-money-commission


open_account()
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 200)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 : {0}, 잔액 : {1}".format(commission, balance))

# 5-3. 기본값


def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, main_lang))


def profile_2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
profile_2("유재석")
profile_2("김태호")


# 5-4. 키워드값
profile(age=20, name="유재석", main_lang="파이썬")


# 5-5. 가변인자
def profile_3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile_3("유재석", 20, "파이썬", "자바", "C", "C++", "C#", "javascript")
profile_3("김태호", 25, "자바", "kotlin", "swift")


# 5-6. 지역변수, 전역변수
gun = 10


# 관리 어려움.
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


# 권장하는 형태
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
