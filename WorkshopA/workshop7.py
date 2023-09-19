def inputValueUser() :
    numberInput = float(input("Insert Your interested Number: "))
    return numberInput

def defineValue() :
    t = "Correct, You are the winner"
    f = "Not Correct!!!"
    return t, f

t,f = defineValue()

def valueCheckAndShow() :
    if inputValueUser() == 25 :
        print(t)
    else :
        print(f)

valueCheckAndShow()