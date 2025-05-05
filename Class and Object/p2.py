class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Debited amount:", amount)
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Credited amount:", amount)
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

# Create an account instance
acc1 = Account(10000, 1234567890)

# Test debit and credit methods
acc1.debit(1000)   # Debited amount: 1000
acc1.credit(500)   # Credited amount: 500
