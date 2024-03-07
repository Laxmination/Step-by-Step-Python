# WAP to check if a list contains a palindrome(a word or sentence that is same from backward or forward) of elements.

list1 =[]
a = (input("Enter first item: "))
b = (input("Enter second item: "))
c = (input("Enter third item: "))
list1.append(a)
list1.append(b)
list1.append(c)
list2 =list1.copy()
list2.reverse()

if(list2 == list1):
    print("Given list is palindrome")
else:
    print("Given list is not palindrom")