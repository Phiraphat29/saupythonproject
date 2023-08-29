product_name = input("Insert product name:")
budget = float(input("Insert budget of product:"))

def productValue(budget) :
    product_real_price = budget + (budget * 10 / 100)
    return "%.2f" % product_real_price

print(f"the price of {product_name} is {productValue(budget)}")