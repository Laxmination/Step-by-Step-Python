# WAP to enter marks of 3 subjects dfrom the users and store them in a dictionary. Start with empty dictionary and add one by one. Use subject Names as key and marks as value.
dict ={}
marks1 =int(input("Enter marks of DAA: "))
dict.update({"DAA": marks1})

marks2 =int(input("Enter marks of DSA: "))
dict.update({"DSA": marks2})

marks3 =int(input("Enter marks of AI: "))
dict.update({"AI": marks3})

print(dict)