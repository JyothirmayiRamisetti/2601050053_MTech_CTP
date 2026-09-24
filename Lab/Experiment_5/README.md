# Experiment 5 – Banking Management System

## Aim

Develop a Banking Management System demonstrating **inheritance and abstraction with full type hints**.

## Algorithm / Procedure

1. Create an abstract `BankAccount` class.
2. Define `deposit` and `withdraw` operations.
3. Create a `SavingsAccount` derived class.
4. Implement the required operations.
5. Display the account balance.

## Program

```python
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
```

## Data & Result

### Output

```text
Withdrawal successful
Balance: 9000
```

## Inference & Analysis

**Abstraction** hides unnecessary implementation details and defines the required operations through the abstract `BankAccount` class.

**Inheritance** allows the `SavingsAccount` class to reuse the properties and methods of the `BankAccount` class.

The program also uses **type hints** for the balance and transaction amounts.

## Result

Thus, a Banking Management System was successfully developed using **abstraction, inheritance, and type hints**.

