# 클래스 정의 및 테스트 코드 통합
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string문법(python 3.6)
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        #부모를 지칭하는 함수
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
def run_tests():
    print("=== Test 1: Person 인스턴스 생성 ===")
    p1 = Person(1, "Alice")
    p1.printInfo()

    print("\n=== Test 2: Manager 인스턴스 생성 ===")
    m1 = Manager(2, "Bob", "CTO")
    m1.printInfo()

    print("\n=== Test 3: Employee 인스턴스 생성 ===")
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()

    print("\n=== Test 4: Person 속성 확인 ===")
    assert p1.id == 1 and p1.name == "Alice"

    print("\n=== Test 5: Manager 속성 확인 ===")
    assert m1.id == 2 and m1.name == "Bob" and m1.title == "CTO"

    print("\n=== Test 6: Employee 속성 확인 ===")
    assert e1.id == 3 and e1.name == "Charlie" and e1.skill == "Python"

    print("\n=== Test 7: Manager는 Person이다 ===")
    assert isinstance(m1, Person)

    print("\n=== Test 8: Employee는 Person이다 ===")
    assert isinstance(e1, Person)

    print("\n=== Test 9: Manager printInfo 오버라이드 확인 ===")
    m1.printInfo()

    print("\n=== Test 10: Employee printInfo 오버라이드 확인 ===")
    e1.printInfo()

    print("\n모든 테스트 통과!")