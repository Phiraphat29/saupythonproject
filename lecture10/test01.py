try :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f"{num1} x {num2} = {result1}")
    print(f"{num1} / {num2} = {result2}")

except ValueError :
    print("Please enter a valid number.")
except ZeroDivisionError :
    print("Cannot Divide by zero.")
except Exception :
    print("Something went wrong. Contact: 0909090909 IT supporter")
finally :
    print("Good Bye!")