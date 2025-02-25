class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.03  # 3% interest rate
 
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance variable for account holder's name
        self.balance = balance  # Instance variable for account balance
 
    # Instance method: To deposit money
    def deposit(self, amount):
        self.balance += amount
        # self.balance = self.balance +amount
        print(f"Deposited {amount}. New balance: {self.balance}")
 
    # Class method: To update the interest rate (can be done globally for all accounts)
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Interest rate updated to: {cls.interest_rate * 100}%")
 
    # Static method: To calculate interest for a given amount (independent of any instance)
    @staticmethod
    def calculate_interest(amount):
        return amount * BankAccount.interest_rate
 
# Using the BankAccount class
 
# Creating an account for John with a balance of 1000
j= BankAccount("John Doe", 1000)
 
# Using instance method to deposit money
j.deposit(500)  # Deposits 500, new balance = 1500
 
# Using class method to update the interest rate
BankAccount.set_interest_rate(0.04)  # Changes interest rate to 4%
 
# Using static method to calculate interest on the balance
interest = BankAccount.calculate_interest(j.balance)
print(f"Interest on John's balance: {interest}")  # Output: 60.0 (4% of 1500)