#Function แบบที่ 2 - Have Parameters/No Return
#parameter คือ ตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้ในฟังค์ชั่นนั่นเท่านั้น

def funcA(x, y) :
    print(f"X is {x}")
    print(f"Y is {y}")
    print(f"Sum {x} + {y} = {x+y}")

funcA(10, 20) #call function ข้อมูลที่ส่งไปให้ parameter เรียกว่า argument อาร์กิวเมนต์
funcA(100, 4000)
print("DTI......")
funcA(50000, 555555)