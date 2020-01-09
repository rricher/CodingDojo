class User:
    def __init__(self, name, rate, balance):
        self.name = name
        self.account = []
        self.account.append(BankAccount(rate, balance))
    def make_deposit(self, account_num, amount):
        self.account[account_num].deposit(amount)
        return self
    def make_withdrawal(self, account_num, amount):
        self.account[account_num].withdraw(amount)
    def display_user_balance(self, account_num):
        print(self.account[account_num].balance())
        return self
    def addAccount(self, rate, balance):
        self.account.append(BankAccount(rate, balance))
        return self
    def transfer_money(self, account_num, other_user, other_users_account, amount):
        self.make_withdrawal(account_num, amount)
        other_user.make_deposit(other_users_account, amount)
        return self

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
    def balance(self):
        return self.account_balance
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.rate
        return self

use1 = User('Ryan', .01, 100)
use2 = User('Rob', .02, 250)
use1.addAccount(.02, 500)
use1.transfer_money(0, use1, 1, 20).display_user_balance(0).display_user_balance(1).transfer_money(1, use1, 0, 20).display_user_balance(0).display_user_balance(1)