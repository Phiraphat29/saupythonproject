#Function 1 : no parameter / no return
def funcA( ) :
    print("AAA")
    #funcB( ) ไม่ควรเรียกฟังค์ชั่นกันไปมา
    print("BBB")
    #ไม่มีคำสั่ง return

def funcB( ) :
    print(111)
    funcA()

funcA( ) 
funcA( ) 
funcB( ) 
funcA( ) 