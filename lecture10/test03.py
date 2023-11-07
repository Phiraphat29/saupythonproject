# writing data(s)
# Open file for writing data(s)
fDTI = open("myfile02.txt", "x", encoding="utf-8") 

fDTI.write("SAU...\n")
fDTI.write("DTI...\n")
fDTI.write("ลาก่อน\n")

fDTI.close()

print("===File saved===")