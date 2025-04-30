class Account:
    def __init__(self, account_holder, bal, acc_no):
        self.account_holder = account_holder
        self.balance = bal
        self.account_no = acc_no
        self.transactions = []

    def debit(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Cannot debit Rs.{amount}")
        else:
            self.balance -= amount
            self.transactions.append(f"Debited Rs.{amount}")
            print(f"Rs.{amount} was debited")
            self.show_balance()

    def credit(self, amount):
        self.balance += amount
        self.transactions.append(f"Credited Rs.{amount}")
        print(f"Rs.{amount} was credited")
        self.show_balance()

    def get_balance(self):
        return self.balance

    def show_balance(self):
        print("Total balance =", self.get_balance())

    def mini_statement(self):
        print(f"\nMini Statement for {self.account_holder} (Acc No: {self.account_no})")
        for txn in self.transactions:
            print(" -", txn)
        print("Current Balance:", self.balance)
