# OOP
class DtiSau:
    # data/property member ค่าช้อมูล
    stuName = ""
    score = ""
    gpa = ""

    # method member คือการทำงาน (function but in class)
    def hiStudent(self):
        print(f"Hi {self.stuName}")

    def showScoreAndGPA(self):
        print(f"score: {self.score} | GPA: {self.gpa}")

# make object
obj01 = DtiSau() # ชื่อคลาสที่มีวงเล็บเป็นการสั่งให้ constructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stuName = "John Doe"
obj01.hiStudent()
obj02.stuName = "Jane Doe"
obj02.score = 99
obj02.gpa = 3.99