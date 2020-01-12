class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(self.account_balance)
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.rate
        return self
acc1 = BankAccount(.01, 100)
acc2 = BankAccount(0.5, 300000)
acc1.deposit(100).deposit(100).deposit(100).withdraw(20).yield_interest().display_account_info()
acc2.deposit(20).deposit(20).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()