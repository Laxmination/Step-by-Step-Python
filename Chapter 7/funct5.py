# WAF to find odd even 
"""
number : function : ODD or EVEN

"""
def oddEven(Num):
    rem =Num %2
    if (rem ==0):
        print("Number is even.")

    else:
        print("Number is odd.")

oddEven(25)
oddEven(30)