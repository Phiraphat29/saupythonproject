# writing data(s)
# Open file for writing data(s)
fDTI = open("myfile03.txt", "a", encoding="utf-8") 

fDTI.write("CCCC\n")
fDTI.write("DDDD\n")

fDTI.close()

print("===File saved===")