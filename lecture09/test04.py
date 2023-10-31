# outstanding property of Encapsulation (ห่อหุ้ม data/ field/ attribute)
class DTITest05 :
    # data
    infoA = 10 # not encapsulation
    __infoB = 20 # encapsulation -> access_modifier = private

    def __init__(self, infoC, infoD):
        self.infoC = infoC # not encapsulation
        self.__infoD = infoD # encapsulation

    # whenever you encapsulate it always have 2 method that is (get, set) from that data
    def setInfoB(self, infoB): # set value for data
        self.__infoB = infoB

    def getInfoB(self): # returns data to use
        return self.__infoB
    
    def setInfoD(self, infoD):
        self.__infoD = infoD

    def getInfoD(self):
        return self.__infoD
    
    def showInfo(self):
        print(self.infoA, end=" ")
        print(self.__infoB, end=" ")
        print(self.infoC, end=" ")
        print(self.__infoD, end=" ")
        print("\n----------")

ob1 = DTITest05(30, 40)
ob2 = DTITest05(30, 100)
ob1.showInfo()
ob1.infoA = 555
ob1.setInfoB(999)
ob1.showInfo()