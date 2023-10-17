# List มีลำดับ (Index)
myList = [10, 20, 10, "Hi", True, [20, "Hello"], (10, 20)]

# Tuple มีลำดับ (Index)
myTuple = (10, 20, 10, "Hi", True, (20, "Hello"), [10, 20], {"SAU", "DTI"})
print(list(myTuple[7])[1]) #อยากได้ DTI

# Set ไม่มีลำดับ (ไม่มี Index)
mySet = {10, 20, 10, "Hi", True, (10, 20)}

# Dictionary ---->> Key:Value / key-> String-Number / Value -> Everything
myDict = {"name": "John Doe", "age": 20, 555:999, "flag": True}
print(myDict["name"])
print(myDict["age"] + myDict[555])
myDict["name"] = "Jane Doe"
myDict["major"] = "DTI"
myDict.pop("name")
myDict.pop(555)
print(myDict)
myDict.popitem()
print(myDict)

for i in myDict :
    print(i, end=" " )

print()

for i in myDict.keys() :
    print(i, end=" ")

print()

for i in myDict.values() :
    print(i, end=" ")

myDict1 = {"a": 10, "b": 20, "c": 30}
myDict2 = myDict1
myDict3 = myDict1.copy()

print()
print(myDict2)
print(myDict3)
myDict2["a"] = 999
myDict3["a"] = 888
print("*****************")
print(myDict1)
print(myDict2)
print(myDict3)