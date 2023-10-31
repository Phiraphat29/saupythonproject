import test06 # user-define module
import math   # build-in module
# import test08
from test08 import calSquareArea, calTriangleArea, calCircleArea


print(f"sum of 10 + 20 = {test06.sumNumber(10, 20)}")

test06.showHi

print(f"product price : 20000฿ | VAT = {2000 * test06.vat}")

print(f"7 power of 15 is {math.pow(7,15)}")

print(f"area of circle radius: 3 is {math.pi * math.pow(3, 2)}")

print(f"area of circle radius: 8 is {calCircleArea(8)}")

print(f"area of square width: 10 lenght: 5 is {calSquareArea(10, 5)}")