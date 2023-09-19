def getStudentNumber() :
    stuNum = int(input("Enter numbers of students: "))
    return stuNum

def gradeCheck(gradeAvg) :
    if gradeAvg > 2.00 :
        return "สอบผ่าน"
    else :
        return "สอบไม่ผ่าน"

def stuLoopAndShow() :
    for i in range(getStudentNumber()):
        stuID = int(input("Enter Student ID: "))
        stuName = input("Enter Student Name: ")
        gradeAvg = float(input("Enter Student Grade Average: "))
        print("================================")
        print("----------GRADE CHECKER---------")
        print(f"{stuID} {stuName} คุณได้เกรด {gradeAvg}  ดังนั้นคุณ{gradeCheck(gradeAvg)}")
        print("================================")
        

stuLoopAndShow()