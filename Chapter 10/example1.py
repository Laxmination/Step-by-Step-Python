import random

x = random.randint(1, 6)
y = random.random()

print(y) # It will print numbers in between 0 and 1
print(x)

mylist=['Rock', 'paper', 'scissors']
z= random.choice(mylist)

Cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

random.shuffle(Cards)

print(Cards)