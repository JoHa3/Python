from models.customer import Customer
from accounts.bank_account import BankAccount
from utils.file_handler import FileHandler

def main():
    customers = FileHandler.load_customers()

    while True:
        print("\n1. Add Customer\n2. Deposit\n3. Withdraw\n4. Manager Login\n5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            cid = input("Customer ID: ")
            acc_num = input("Account Number: ")

            customer = Customer(name, email, cid)
            account = BankAccount(acc_num)
            customer.add_account(account)

            customers.append(customer)
            FileHandler.save_customers(customers)
            print("Customer added.")

        elif choice == "2":
            acc = input("Account Number: ")
            amt = float(input("Amount: "))
            for c in customers:
                for a in c.accounts:
                    if a.account_number == acc:
                        a.deposit(amt)
                        FileHandler.save_customers(customers)
                        print("Deposited.")
                        break

        elif choice == "3":
            acc = input("Account Number: ")
            amt = float(input("Amount: "))
            for c in customers:
                for a in c.accounts:
                    if a.account_number == acc:
                        try:
                            a.withdraw(amt)
                            FileHandler.save_customers(customers)
                            print("Withdrawn.")
                        except Exception as e:
                            print(e)

        elif choice == "4":
            from models.manager import Manager
            mgr = Manager("001", "Admin")
            print("\n1. View Customers\n2. View Logs")
            mopt = input("Choice: ")
            if mopt == "1":
                mgr.view_customers()
            elif mopt == "2":
                mgr.view_logs()

        elif choice == "5":
            FileHandler.save_customers(customers)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
