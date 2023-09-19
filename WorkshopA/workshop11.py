def getUserDetails() :
    userName = input("Enter the name of user: ")
    userTel = float(input("Enter the user tel.: "))
    userTime = float(input("Enter the time of using telephone in minute: "))
    return userName, userTel, userTime

userName, userTel, userTime = getUserDetails()

def calculateServiceCost() :
    if userTime >= 1 and userTime < 16 :
        serviceCost = userTime * 5
    elif userTime >= 16 and userTime < 31 :
        serviceCost = userTime * 3
    else :
        serviceCost = userTime * 1.5 
    return serviceCost

def showServiceCost() :
    print(f"{userName} tel.{userTel} you got service charge {calculateServiceCost()}")

showServiceCost()