class BankAccount(object):
    account_count = 1000

    def __init__(self, account_holder):
        self.account_number = BankAccount.account_count
        BankAccount.account_count += 1
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, user_deposit):
        self.balance += user_deposit

    def withdraw(self, user_withdraw):
        if user_withdraw > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= user_withdraw

    def get_balance(self):
        print(f"Name: {self.account_holder}")
        print(f"{self.account_holder}'s Acc Number: {self.account_number}")
        print(f"Current balance: {self.balance}\n")

    @staticmethod
    def is_valid_number(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def interest(self):
        self.overall_interest = self.balance * self.interest_rate
        self.balance += self.overall_interest
        return self.balance
    
    def print_interest_amount(self):
        print(f"Interest Amount: {self.overall_interest}")
    

class Bank(object):
    pass
    # jamie_account = BankAccount("Jamie Doyle")
    # jamie_account.deposit(1000)
    # jamie_account.get_balance()
    # jamie_account.withdraw(250)
    # jamie_account.get_balance()

    # karl_account = BankAccount("Karl Doyle")
    # karl_account.deposit(1002)
    # karl_account.get_balance()
    # karl_account.withdraw(5)
    # karl_account.get_balance()

    # jamie_saving_account = SavingsAccount("Jamie Doyle (Savings Account)", 0.05)
    # jamie_saving_account.deposit(1000)
    # jamie_saving_account.get_balance()

    # jamie_saving_account.withdraw(150)
    # jamie_saving_account.get_balance()

    # jamie_saving_account.interest()
    # jamie_saving_account.get_balance()

    # jamie_saving_account.print_interest_amount()





if __name__ == "__main__":
    Bank()





    




