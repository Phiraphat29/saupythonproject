# calculate triangle
# มองหา feature การทำงานว่ามีอะไรบ้างเพื่อจะไปสร้างเป็น function

def inputBaseHeight():
    base = float(input("enter base: "))
    height = float(input("enter height: "))
    return base, height

def calAndShow(base, height):
    area = base * height / 2
    print(f"This triangle has {base} base and {height} height, so the area is {area}")

print("--------------------------------")
print("--* Calculate Triangle Area *--")
print("--------------------------------")

base, height = inputBaseHeight()

calAndShow(base, height)

    