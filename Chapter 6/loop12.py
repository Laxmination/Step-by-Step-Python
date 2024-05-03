rows = int(input("How many Rows? "))
Column = int(input("How many columns? "))
symbole = input("Enter a symbole: ")

for i in range(rows):
    for j in range(Column):
        print(symbole, end="") 
    print()