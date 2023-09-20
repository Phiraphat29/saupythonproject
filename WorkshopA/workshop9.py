def getEmpDetails() :
    empID = int(input("Enter Employee ID: "))
    empName = input("Enter Employee Name: ")
    empSales = float(input("Enter Employee Sales in Baht: "))
    return empID, empName, empSales

empID, empName, empSales = getEmpDetails()

def commissionCheckAndCal() :
    if empSales < 1000 :
        commission = 0
    elif empSales < 2001 :
        commission = empSales * 1 / 100
    elif empSales < 3001 :
        commission = empSales * 3 / 100
    else :
        commission = empSales * 5 / 100
    return commission

def showCommission() :
    print(f"{empID} {empName} you got a commission {commissionCheckAndCal()} baht.")

showCommission()