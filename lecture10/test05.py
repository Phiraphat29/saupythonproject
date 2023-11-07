# Read data from file(s)
fDTI = open("myfile01.txt", "r", encoding="utf-8")

try :
    data = fDTI.read()
    print(data)

except Exception :
    print("Contact Admin: 00000000000")
finally :
    fDTI.close()