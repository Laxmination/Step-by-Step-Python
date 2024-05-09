def hello(**sajjan):
    print("Hello,", end=" ")
    for key, value in sajjan.items():
        print(value, end=" ")


hello(title="Ms.", firstName="Ankita", middleName="Kumari", lastName="Jha", gratitude="Sister")