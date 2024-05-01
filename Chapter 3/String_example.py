#WAP to find the occurrence of 's' in String.
B ="string"
A ="STrInG"
print(B)
print(B.count("s"))
print(B *3) # it will print string 3 times
print(B.isalpha()) # It gives true 
print(B.isdigit()) # It gives false
print(B.capitalize()) # the first letter will be capital
print(B.upper()) # all letters will be in upper case
print(A.lower()) # all letters will be in lower case
print(B.replace("t", "p")) # It will replaces t with p
print(B[0:4]) # This function will display the string character from 0 to 3
print(B[0:7:3]) # It will display the string character third after previous character [Start:stop:step]
print(B[::2]) # It will display the string character second after the previous character
print(B[::-1]) # It reverses the string and display

website = "http://google.com"
website2 ="http://twitter.com"

slice = slice(7, -4) # slices the string and return the sliced piece

print(website[slice]) 
print(website2[slice])