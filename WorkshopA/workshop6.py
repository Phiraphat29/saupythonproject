def getBorrowerDetails() :
    borrowerName = input("Enter Borrower Name: ")
    borrowerMoneyBorrowed = float(input("Enter Borrower money borrowed: "))
    return borrowerName,borrowerMoneyBorrowed

borrowerName,borrowerMoneyBorrowed = getBorrowerDetails()

def interestCalculate() :
    if borrowerMoneyBorrowed > 1000 :
        interest = 2.5 / 100 * borrowerMoneyBorrowed
    else :
        interest = 5.5 / 100 * borrowerMoneyBorrowed
    return interest

def showInterest() :
    print(f"{borrowerName} you have to pay {interestCalculate()}")

showInterest()