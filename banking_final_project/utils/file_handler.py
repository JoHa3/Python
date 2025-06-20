import json
import os

class FileHandler:
    FILE_PATH = 'data/customers.json'

    @staticmethod
    def save_customers(customers):
        data = []
        for c in customers:
            customer_data = {
                "customer_id": c.customer_id,
                "name": c.name,
                "email": c.email,
                "accounts": [{
                    "account_number": a.account_number,
                    "balance": a.balance
                } for a in c.accounts]
            }
            data.append(customer_data)

        with open(FileHandler.FILE_PATH, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_customers():
        from models.customer import Customer
        from accounts.bank_account import BankAccount

        if not os.path.exists(FileHandler.FILE_PATH):
            return []

        with open(FileHandler.FILE_PATH, 'r') as f:
            data = json.load(f)

        customers = []
        for item in data:
            c = Customer(item["name"], item["email"], item["customer_id"])
            for acc in item["accounts"]:
                a = BankAccount(acc["account_number"], acc["balance"])
                c.add_account(a)
            customers.append(c)
        return customers
