def getGroupDetails():
    leader = input("Enter name of leader: ")
    leaderNumber = input("Enter leader number: ")
    tourist = int(input("Enter number of tourist: "))
    return leader, leaderNumber, tourist

leader, leaderNumber, tourist = getGroupDetails()

def calculatePackage() :
    if tourist >= 1 and tourist < 3 :
        package = tourist * 300
    elif tourist >= 3 and tourist < 6 :
        package = tourist * 250
    elif tourist >= 6 and tourist < 11 :
        package = tourist * 210
    else :
        package = tourist * 150
        return package

def showPackage():
    print(f"Leader {leader} Phone Call {leaderNumber} you have {tourist} tourist and the package is {calculatePackage()} baht")

showPackage()