# animal1 = "fox"
# animal2 = "dog"
 

# print("A quick brown", animal1, "jumps over the lazy", animal2) # Output without using string format 
# print("A quick brown {animal3} jumpes over the lazy {animal4}".format(animal3="Jackel", animal4="dog")) # output using string format
# print("A quick brown {1} jumpes over the lazy {0}".format(animal1, animal2)) # Positional argument

# text = "Hello Users, here I am {}"
# print(text.format("Laxmi"))
# print("Hello Users, here I am {:10}. Nice to meet you".format("Laxmi"))
# print("Hello Users, here I am {:<10}. Nice to meet you".format("Laxmi"))
# print("Hello Users, here I am {:>10}. Nice to meet you".format("Laxmi"))
# print("Hello Users, here I am {:^10}. Nice to meet you".format("Laxmi"))

number = 6.6767676767676767
number1 =10000000
print("The number is {:.2f} after roundof".format(number))
print("The number is {:,}".format(number1))
print("The number is {:b} in binary".format(number1))
print("The number is {:o} in octal".format(number1))
print("The number is {:X} in hexadecimal".format(number1))
print("The number is {:E} in scientific notation".format(number1))