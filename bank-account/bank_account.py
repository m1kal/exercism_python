import threading

class BankAccount:
    def __init__(self):
        self.active = False
        self.balance = 0
        self.lock = threading.Lock()

    def assert_(self, condition, amount, limit = False):
        if not condition or amount < 0 or (limit and amount > self.balance):
            raise ValueError('Invalid operation')

    def get_balance(self):
        self.assert_(self.active,0)
        return self.balance

    def open(self):
        self.assert_(not self.active,0)
        self.active = True
        self.balance = 0

    def deposit(self, amount):
        self.assert_(self.active,amount)
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        self.assert_(self.active,amount,True)
        with self.lock:
            self.balance -= amount

    def close(self):
        self.assert_(self.active,0)
        self.active = False


