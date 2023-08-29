box_width = float(input("Enter width of room in cm: "))
box_lenght = float(input("Enter length of room in cm: "))
box_height = float(input("Enter height of room in cm: "))
print("--------------------------------")
#คำนวณ
total_area = ((box_width * box_lenght) * 2)+  ((box_width * box_height) * 2) +  ((box_height * box_lenght) * 2)
gallon_amount = round(total_area / 5)
print(f"The box that have {box_lenght} long {box_width} wide and {box_height} tall should have {gallon_amount} gallon")
print("The box that have" , box_lenght , "long" , box_width , "wide and" , box_height , "tall should have", gallon_amount, "gallon")
print("The box that have " + str(box_lenght) + " long " + str(box_width), "wide and " + str(box_height) + " tall should have " + str(gallon_amount) + " gallon ")
print("The box that have {} long {} wide and {} tall should have {} gallon".format((box_lenght), (box_width), (box_height), (gallon_amount)))
      





