# Delete file(s)
import os

if os.path.exists("myfile01.txt"):
    os.remove("myfile01.txt")
    print("File deleted")
else :
    print("No file to delete.")