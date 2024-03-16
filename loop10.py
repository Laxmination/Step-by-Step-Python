# n =int(input("Enter any number: "))
# fac = 1
# i =1

# while i <= n:
#     fac *= i
#     i +=1

# print("Factorial of given number is -> ", fac)



n =int(input("Enter range of numbers: "))
fac = 1

for i in range(1, n+1):
    fac *=i

print("Factorial of given number is -> ", fac)