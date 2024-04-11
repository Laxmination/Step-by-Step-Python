# password of account using private attribute
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # acc_pass is made private by using __ infront of acc_pass

    def reset_pass(self):
        print(self.__acc_pass) # acc_pass is accessed here

acc1 = Account("12345", "abcsed")

print(acc1.acc_no)
print(acc1.reset_pass())
print(acc1.__acc_pass) # acc_pass cannot be accessed here because it is made private