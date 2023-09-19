def inputX():
     x = float(input("Enter the Value of x : "))
     return x

x = inputX()

def calculate():
     y = 2 * x ** 2 + 2 * x + 1
     return y

def showCal():
      print(f"The value of y is {calculate()}")

showCal()
    
