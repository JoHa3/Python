from models.person import Person

class Customer(Person):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)  # Inherit from Person
        self.customer_id = customer_id
        self.accounts = []  # List of BankAccount objects

    def add_account(self, account):
        self.accounts.append(account)

