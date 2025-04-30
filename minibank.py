class account :
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no= acc


    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance=", self.get_balance())

    def credite(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())


    def get_balance(self):
        return self.balance
    

acc1 = account(1000, 1234)
acc1.debit(1000)
acc1.credite(500)
acc1.credite(40000)