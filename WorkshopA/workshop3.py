def getProductDetails() :
    productName = input("Enter product name: ")
    productPrice = float(input("Enter product price: "))
    return productName, productPrice

productName, productPrice = getProductDetails()

def calculate():
    tax = productPrice * 7 / 100
    return tax

def showCal() :
    print(f"Tax of product is {calculate()} baht")

showCal()