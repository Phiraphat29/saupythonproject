# List Method
var1 = [10, 20, "Hello", True, [111, "Wow"], "มานะ"]

# append เพิ่ม 1 ข้อมูล
var1.append(555)
var1.append(["Hi", "Hey", 999])
print(var1)

# Extend เพิ่มแต่ละข้อมูล
var1.extend([10, 20, 30])
print(var1)

# remove ลบข้อมูล
var1.remove("Hello")
var1.remove(10)
print(var1)

# -----------------------------
var2 = [1, 20, "Hello"]
# insert แทรกข้อมูลในหมายเลขอินเด็กซ์ที่เราต้องการ
var2.insert(2, "Hi")
print(var2)

# pop ระเบิดตัวข้างในจากฝั่งขวาสุด (เลือกได้)
var2.pop()
print(var2)
var2.pop(1)
print(var2)

# index ชี้ว่าข้อมูลนั้นอยู่ใน index ที่เท่าไหร่
print(var2.index("Hi"))

# count นับข้อมูลใน list
print(var1.count(10))
var3 = [10, 10, 20, "Hi", 10, "HI"]
print(f"ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว")
print(f"ใน var3 มี Hi ทั้งหมด {var3.count('Hi')} ตัว")
print('Hi \'SAU\'')
print("Hi 'SAU'")
print("Hi \"DTI\"")
print('Hi "DTI"')

# Method ต่อไปนี้ใช้ได้แค่ข้อูลประเภทเดียวกันเท่านั้น
# sort จัดเรียงข้อมูลใน list
var4 = [10, 10, 20, "Hi", 10, "HI"]
# var4.sort() = error
var5 = [99, 34, 635, 3423, 99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse = True)
print(var5)