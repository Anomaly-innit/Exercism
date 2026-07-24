class BankAccount:
    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        if not self.is_open:
            raise ValueError('account not open')
            
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError('account already open')
        self.is_open = True
        self.balance = 0
        return self.is_open

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if not self.is_open:
            raise ValueError('account not open')
        
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if not self.is_open:
            raise ValueError('account not open')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
            
        self.balance -= amount
        return self.balance

    def close(self):
        if self.is_open == False:
            raise ValueError('account not open')
            
        self.is_open = False
        return self.is_open