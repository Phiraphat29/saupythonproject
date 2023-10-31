# constructor

class DTITest03 :
    # data
    infoA = 10
    
    # constructor will make object that made from the same class have a different feature
    # constructure will always work when object has been made
    def __init__(self, infoB, infoC) :
        self.infoB = infoB
        self.infoC = infoC
        print("Wow wow wow....")

    # method
    def showMixAndInfo(self, mix) :
        print(self.infoA + self.infoB + self.infoC + mix)

# make object
sau1 = DTITest03(20, 30)
sau2 = DTITest03(10, 100)
sau3 = DTITest03(20, 30)