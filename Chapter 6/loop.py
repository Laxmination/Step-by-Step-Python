# while True:
#     name = input("What is your Name: ")
#     if name != "":
#         break

phoneNumber = "+977-983-456-5678"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")