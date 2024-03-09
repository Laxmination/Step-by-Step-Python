#WAP to find greatest of 3 numbers entered by the user.
num1 =int(input("Enter First number:"))
num2 =int(input("Enter Second number:"))
num3 =int(input("Enter Third number:"))

if(num1 >num2 and num1 >num3):
    print("First number is the greatest number")
elif(num2 >num3):
    print("Second number is the greatest number")
else:
    print("Third number is the greatest.")