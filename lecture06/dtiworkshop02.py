def getCardetail() :
     registration = input("Enter car registrations: ")
     weight = float(input("Enter your car weight: "))
     return registration, weight

def checkCarAndShow(registration, weight) :
    if weight > 1000 :
        print(f"รถทะเบียน {registration} น้ำหนัก {weight} รถคันนี้ไม่ผ่านเกณฑ์")
    else :
        print(f"รถทะเบียน {registration} น้ำหนัก {weight} รถคันนี้ผ่านเกณฑ์")

print("--------------------------------")
print("--* Truck Checker *--")
print("--------------------------------")

registration, weight = getCardetail()

checkCarAndShow(registration, weight)

