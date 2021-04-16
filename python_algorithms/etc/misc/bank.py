def details(fn):
    def wrapper(self, *args):
        fn(self, *args)
        print(repr(self))
    return wrapper

class Account:
    def __init__(self):
        self.balance = 0

    @details
    def withdraw(self, amt):
        self.balance -= amt

    @details
    def deposit(self, amt):
        self.balance += amt

class MinBalAccount(Account):

    @details
    def __init__(self, min_balance):
        Account.__init__(self)
        self.min_balance = min_balance


    @details
    def withdraw(self, amt):
        if self.balance - amt < self.min_balance:
            print("Sorry, min balance must be maintained")
        else:
            Account.withdraw(self, amt)

    def __repr__(self):
        return f'| Bal: {self.balance} |\n| MinBal: {self.min_balance}|\n'

# account = MinBalAccount(100)
# print(account.deposit(1000))
# print(account.withdraw(50))

account = MinBalAccount(25)
# print(repr(account))
account.deposit(1000)
# print(repr(account))

account.withdraw(50)
# print(repr(account))
