import os

path = "C:\\Users\\Laxmi\\Desktop\\test.txt"

if os.path.exists(path):
    print("This location exists in this OS:)")

else:
    print("This location does not exist in this windows:(")