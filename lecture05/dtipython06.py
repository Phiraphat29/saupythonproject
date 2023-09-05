#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง การบ่งบอกว่าการทำงานนั้น ๆ ทำเสร็จแล้ว
def example1():
    print(111)
    print(222)
    return
    print(3333)
    print(4444)
    return 

#Default Parameter มีการกำหนดค่าเริ่มต้นให้กับ parameter
def dtiTest(x, y, z = 20 , a = 10) :
    print(f"{x} + {y} + {z} + {a} = {x+y+z+a} ")


dtiTest(5, 100)

dtiTest(9, 8, 10)