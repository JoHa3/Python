from datetime import datetime

class TransactionLogger:
    @staticmethod
    def log(account_number, action, amount):
        with open('data/transaction_log.txt', 'a') as file:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{time} | {account_number} | {action} ${amount:.2f}\n")

