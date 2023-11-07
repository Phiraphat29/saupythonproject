# writing data(s)
# Open file for writing data(s)
fDTI = open("myfile01.txt", "w", encoding="utf-8") 

fDTI.write("WOW...\n")
fDTI.write("Woo...\n")
fDTI.write("ลาก่อน\n")

fDTI.close()

print("===File saved===")