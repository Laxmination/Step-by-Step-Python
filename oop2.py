# Create Account class with 2 attributes - balance and account no. and create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount,"is debited")
        print("Total balance =Rs.", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited")
        print("Total balance = Rs.", self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 =Account(100000, 9123456)
acc1.debit(50000)
acc1.credit(10000)
