class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return self.owner

    def __str__(self):
        return self.balance

    def deposit(self, money_dep):
        self.balance += money_dep
        print("money accepted")

    def withdraw(self, money_wd):
        if self.balance >= money_wd:
            self.balance -= money_wd
            print("money withdrawn")
        else:
            print("overdrawn")


a = Bank("amina", 100)
a.deposit(50)
print(a.balance)
a.withdraw(100)
print(a.balance)




