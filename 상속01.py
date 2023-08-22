# 부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("{0} 현재 작업중".format(self.name))
    
    def coding(self):
        print("{0} 현재 코딩중".format(self.name))

# 자식 클래스 정의
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()
s.working()
s.coding()
