class BankAccount:
    def __init__(self, account_number, account_holder, balance=0): # konstruktor
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance = self.balance - amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            print("Invalid target account.")
            return
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return

        self.balance = self.balance - amount
        target_account.balance = target_account.balance + amount
        print(f"Transferred {amount} to {target_account.account_holder}")
        print(f"Your new balance: {self.balance}")

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance})"

# OOP muhim konseptsiya 1: Inheritance - Merosxo'rlik
# --- Child Class 1 ---
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)

        self.interest_rate = interest_rate
        self.withdrawal_limit = 3  # per session (simplified)
        self.withdrawals_made = 0
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")

    # OOP muhim konseptsiya 2: Polymorphism
    # Polymorphism: overriding withdraw()
    def withdraw(self, amount):
        if self.withdrawals_made >= self.withdrawal_limit:
            print("Withdrawal limit reached for savings account.")
            return
        
        super().withdraw(amount)
        self.withdrawals_made += 1


# --- Child Class 2 ---
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism: different withdraw logic
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        # allow overdraft
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
            return
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")



acc1 = BankAccount("001", "Alibek", 1000)
acc2 = BankAccount("002", "Bob", 500)
acc3 = BankAccount("003", "Asilbek")

# print(acc1)
# print(acc2)
# print(acc3)

# acc3.deposit(5000)
# acc3.check_balance()

# acc1.withdraw(200)
# acc1.check_balance()

# acc3.transfer(acc2, 1000)
# acc3.check_balance()
# acc2.check_balance()

acc4 = SavingsAccount("004", "Gulruh", 0.1)
acc4.deposit(3000)
#acc4.add_interest()


# acc1.withdraw(200)
# acc1.withdraw(250)
# acc1.withdraw(250)
# acc1.withdraw(100)
# acc1.withdraw(100)

acc4.withdraw(200)
acc4.withdraw(250)
acc4.withdraw(250)
acc4.withdraw(100)
acc4.withdraw(100)

# acc3.deposit(100000)
# print(acc3)

# acc3.withdraw(90000)
# print(acc3)

# acc3.check_balance()

# acc3.transfer(acc1, 1)
# print(acc3)
# print(acc1)

# acc1.deposit(200)
# acc1.withdraw(150)
# acc1.transfer(acc2, 300)

# acc1.check_balance()
# acc2.check_balance()

# print(acc1)

# acc4 = SavingsAccount("004", "Mirfayz", 2000)
# acc4.deposit(5000)
# acc4.check_balance()

# acc4.add_interest()
# acc4.check_balance()

# acc5 = CheckingAccount("005", "Mirfayz", 500)
# acc5.withdraw(30)
# acc5.check_balance()

# acc5.withdraw(700)
# acc5.check_balance()

# # limit exceeded
# acc5.withdraw(700)
# acc5.check_balance()