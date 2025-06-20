from models.employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id, name)

    def view_customers(self, customers):
        for cust in customers:
            print(f"{cust.customer_id}: {cust.name}, {cust.email}")

    def view_logs(self, log_file='data/transaction_log.txt'):
        with open(log_file, 'r') as f:
            print(f.read())
