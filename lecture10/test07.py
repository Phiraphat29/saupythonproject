# Read data from file(s)
fDTI = open("myfile01.txt", "r", encoding="utf-8")

try :
    data = fDTI.read()

    for dataByLine in data :
        print(dataByLine, end = "")

except Exception :
    print("Contact Admin: 00000000000")
finally :
    fDTI.close()