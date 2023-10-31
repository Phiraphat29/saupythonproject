# outstanding property : inheritance (สืบทอด) is when one class inherit other one class *** (RE-USE)
# inherit have super class (parent) and sub class (child)
# what does super class have the sub class is same

# outstanding property : polymorphism (พ้องรูป) same behavior but different method (sub class take method of super class but modify it)
class SAU01:
    infoA = 10

    def showHi():
        print("Hi...")

class SAU02(SAU01): # inherited
    infoB = 20

    def showHey():
        print("Hey...")

    #overiding method : polymorphic
    def showHi():
        print("Hi Hi Hi...")

obj1 = SAU01()
obj2 = SAU02()
