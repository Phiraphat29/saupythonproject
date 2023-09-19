def getStuDetails() :
    stuID = int(input("Enter Student ID: "))
    stuName = input("Enter Student Name: ")
    stuResultFirst = float(input("Enter Student 1st Result: "))
    stuResultSecond = float(input("Enter Student 2nd Result: "))
    stuResultThird = float(input("Enter Student 3rd Result: "))
    return stuID, stuName, stuResultFirst, stuResultSecond, stuResultThird

stuID, stuName, stuResultFirst, stuResultSecond, stuResultThird = getStuDetails()

def calAvgScore() :
    return  (stuResultFirst + stuResultSecond + stuResultThird) / 3

def showResult() :
    print(f"{stuID} {stuName} you have average score {calAvgScore():.2f}")

showResult()