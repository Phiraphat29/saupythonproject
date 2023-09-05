#โปรแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวง และปรืมาตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาณทางหน้าจอ

#ขอ 5 ฟังก์ชั่น
import math

def getRadius() :
    return float(input("enter radius of circle: "))

def calCircleArea(radius) :
    return math.pi * radius * radius

def calCirclePerimeter(radius) :
    return 2 * math.pi * radius

def calCircleVolume(radius) :
    return 4/3 * math.pi * radius * radius * radius

def showCal() :
    radius = getRadius()
    area = calCircleArea(radius)
    perimeter = calCirclePerimeter(radius)
    volume = calCircleVolume(radius)
    print("Radius: " "%.4f" %  radius)
    print("Area: " "%.4f" % area)
    print("Perimeter: " "%.4f" % perimeter)
    print("Volume: " "%.4f" % volume)


showCal()
