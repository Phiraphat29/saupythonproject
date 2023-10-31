# destructor

class DTITest04 :
    data1 = 10

    # constructor
    def __init__(self, data2) :
        self.data2 = data2
        print("Hi...")

    def doTask1(self):
        print("^_^")

    def doTask2(self, value):
        print(value)

    # destructor
    def __del__(self):
        print("Goodbye....")

# ----------------------------------------------
sauA = DTITest04(20)    
sauB = DTITest04(30)    
sauC = DTITest04(20)    

sauC.doTask2("T_T") #T_T
sauC.doTask1() #^_^
print(sauA.data1 + sauB.data1) #20