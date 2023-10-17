# List มีลำดับ (Index)
myList = [10, 20, 10, "Hi", True, [20, "Hello"]]
print(myList)
print(len(myList))

# Tuple มีลำดับ (Index)
myTuple = (10, 20, 10, "Hi", True, (20, "Hello"))
print(myTuple)
print(len(myTuple))

# Set ไม่มีลำดับ (ไม่มี Index)
mySet = {10, 20, 10, "Hi", True, (20, "Hello")}
print(mySet)
print(len(mySet))

for i in mySet :
    print(i, end="/")
print("\n-------------------------")

listFromSet = list(mySet)
print(listFromSet)
listFromSet[0] = "DTI"
mySet = set(listFromSet)
print(mySet)

mySet.clear()
print(len(mySet))

mySet1 = {10, 20, 30, "Hi"}
mySet2 = {10, "Hello", "Hi", True}

mySet1.add(999)
print(mySet1)
mySet1.remove("Hi")
print(mySet1)

print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))

# len, min, max
print(min(mySet2))