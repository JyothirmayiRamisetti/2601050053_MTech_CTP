from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def show_balance(self) -> None:
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

account = SavingsAccount(10000)
account.deposit(2000)
account.withdraw(3000)
account.show_balance()
