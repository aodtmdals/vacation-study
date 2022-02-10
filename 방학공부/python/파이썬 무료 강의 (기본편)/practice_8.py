# 8-1 ~ 8-3
# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))


# 8-4. 메소드
# 공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)


# 8-5. 상속, 8-6. 다중 상속
class Unit1:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit1(Unit1):
    def __init__(self, name, hp, damage):
        Unit1.__init__(self, name, hp)
        self.damage = damage

    def attack1(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"
              .format(self.name, location, self.damage))

    def damaged1(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit1, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit1.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


firebat1 = AttackUnit1("파이어뱃", 50, 16)
firebat1.attack1("5시")

firebat1.damaged1(25)
firebat1.damaged1(25)

valkytie = FlyableAttackUnit("발키리", 200, 6, 5)
valkytie.fly(valkytie.name, "3시")

# 8-7. 메소드 오버라이딩


class Unit2:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))


class AttackUnit2(Unit2):
    def __init__(self, name, hp, speed, damage):
        Unit2.__init__(self, name, hp, speed)
        self.damage = damage

    def attack1(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]"
              .format(self.name, location, self.damage))

    def damaged1(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class Flyable1:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit1(AttackUnit2, Flyable1):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, 0, damage)
        Flyable1.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit2("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit1("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")


# 8-8. pass
class BuildingUnit(Unit2):
    def __init__(self, name, hp, speed):
        def __init__(self, name, hp, location):
            # 아무것도 안하고 넘어감
            pass


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# 8-9. super


class BuildingUnit(Unit2):
    def __init__(self, name, hp, location):
        # 방법1
        #Unit2.__init__(self, name, hp, 0)
        # 방법2 (다중상속 X)
        super().__init__(name, hp, 0)
        self.location = location


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
