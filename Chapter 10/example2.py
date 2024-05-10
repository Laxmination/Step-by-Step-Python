try:
    a = int(input("Enter a number: "))
    b = int(input("Enter anpther number: "))
    result = a /b

except ZeroDivisionError as e:
    print("Zero le divide garna sakdainau! murakh!")
    print(e)
except ValueError as v:
    print("Enter only numbers idiot!")
    print(v)
except Exception:
    print("Something went wrong:(")

else:
    print(result)