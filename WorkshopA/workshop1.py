def getProductDetails() :
    productName = input("Enter product name: ")
    productPrice = float(input("Enter product price: "))
    return productName, productPrice

def calculatePrice() :
    productRealPrice = productPrice + (productPrice * 10 / 100)
    return productRealPrice

def showPrice() :
    print(f"The {productName} is {calculatePrice()} baht")

productName, productPrice = getProductDetails()

showPrice()