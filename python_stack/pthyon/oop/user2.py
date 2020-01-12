class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
use1 = User('ryan', 'ryan')
use2 = User('ryan2', 'ryan2')
use3 = User('ryan3', 'ryan3')
use1.make_deposit(200).make_deposit(30).make_deposit(200).make_withdrawal(45).display_user_balance()
use2.make_deposit(500).make_deposit(1299).make_withdrawal(2).make_withdrawal(42).display_user_balance()
use3.make_deposit(2500).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()
use1.transfer_money(use3, 200).display_user_balance()
use3.display_user_balance()
