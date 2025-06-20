from transactions.transaction_logger import TransactionLogger
from builtins import ValueError

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        TransactionLogger.log(self.account_number, "Deposit", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        TransactionLogger.log(self.account_number, "Withdraw", amount)
