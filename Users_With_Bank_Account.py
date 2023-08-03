
"""
Assignment: Users With Bank Accounts

Create a User class that has an association with the BankAccount class. You should not have to change anything in the BankAccount class.

For example, from the User class we should be able to deposit money into the user's account:
But our User class does not have a self.account_balance attribute. What it does have is an instance of a BankAccount by the name of self.account. That means that we'll be mirroring the methods created in the BankAccount class like make_deposit (and other methods referencing self.account_balance). But we'll be calling on the BankAccount class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.

Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:
class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    print(self.account.balance)		# or access its attributes
"""
class User:
    def __init__(self, name,):
        self.name = name
        self.account = Bank_Account(int_rate=0.01, balance=0)

    def deposit(self, amount):
        self.account.deposit(amount)
        print(f"Made Deposit {amount} to {self.name} account")
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"Withdrew ${amount} from {self.name} account")
        return self
    
    def displayUserBalance(self):
        print(f"Retrieving {self.name} balance")
        print(f"{self.name} Balance {self.account.balance}")

class Bank_Account:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee will deduct $5")
            self.balance = self.balance - 5
        return self

    def displayAccountInfo(self):
        print(f"Balance:{self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("You have a negative account balance.")
        return self


Ryan1 = User("Ryan")
Kevin2 = User("Kevin")
Mike3 = User("Mike")

print("*" * 40)


Ryan1.displayUserBalance()
Ryan1.deposit(5000).withdraw(500).withdraw(3000).deposit(2000).withdraw(200).displayUserBalance()

print("*" * 40)

Kevin2.displayUserBalance()
Kevin2.deposit(50).withdraw(10).withdraw(10).deposit(10).withdraw(500).displayUserBalance()

print("*" * 40)

Mike3.displayUserBalance()
Mike3.deposit(50000).withdraw(1000).withdraw(500).deposit(20000).withdraw(300).displayUserBalance()







