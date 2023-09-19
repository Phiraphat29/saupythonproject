def getOfficerDetails() :
    officerID = int(input("Enter Officer ID: "))
    officerName = input("Enter Officer Name: ")
    officerSalary = float(input("Enter Officer Salary: "))
    return officerID,officerName,officerSalary

officerID,officerName,officerSalary = getOfficerDetails()

def netSalaryCalculate() :
    netSalary = officerSalary - (officerSalary * 7 / 100) - 500
    return netSalary

def showNetSalary() :
    print(f"{officerID} {officerName} you got net salary {netSalaryCalculate()} baht")

showNetSalary()
