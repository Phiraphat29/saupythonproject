money = input("insert number of money : ")
amount_of_people = input("insert amount of people : ")
product_value = int(money)/int(amount_of_people)
product_value_text = format(product_value, ".2f")
print("You would get", product_value_text, "Baht per person") 
print("You would get " + product_value_text + " Baht per person")
print("You would get {} Baht per person".format(product_value_text)) 
print(f"You would get {product_value_text} Baht per person")