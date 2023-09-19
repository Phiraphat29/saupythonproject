def getProvince() :
    province = input("Enter the province: ")
    return province

def getPH():
    ph = int(input("Enter PH: "))
    return ph

def phCheck() :
    getProvince()
    ph = getPH()
    if ph >= 7 and ph < 9 :
        print("Result is Normal")
    elif ph > 8 :
        print("Result is Acid")
    else :
        print("Result is Alkali")

phCheck()