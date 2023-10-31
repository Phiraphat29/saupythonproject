class DTITest01 :
    pass

class DTITest02 :
    # data/attribute/property/field is type of variable
    infoA = ""
    infoB = 20

    # method is type of function
    def showHi(self) :
        print("Hi...")

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)

# make an object
objA = DTITest02()
objB = DTITest02()
joodoe = DTITest02()

objA.infoA = "XXXX"
objB.infoB = 100

print(objA.infoB + objB.infoB)

joodoe.showInfoAandB()