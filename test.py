class BankAccount():
   
   int account_number
   string account_holder
   double balance

   deposit(), 
   withdraw(), 
   get_balance()





# 1. BankAccount Class:
#    - Attributes: account_number, account_holder, balance
#    - Methods: deposit(), withdraw(), get_balance()


2. Bank Class:
   - Attributes: accounts (a list to store BankAccount objects)
   - Methods: add_account(), get_account_details(), calculate_interest(), view_all_accounts()


3. SavingsAccount Class (Inherits from BankAccount):
   - Additional Attributes: interest_rate
   - Methods: calculate_interest()


4. User Interface:
   - A simple console-based interface to interact with the banking system.
   - Display a menu with options to create an account, deposit, withdraw, view account details, calculate interest, and exit.
