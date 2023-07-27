bank_accounts = {
    1: {'name': 'Jamie Doyle', 'type': 'Checking', 'balance': 1000.00},
    2: {'name': 'Karl Doyle', 'type': 'Buisness', 'balance': 750.00},
    3: {'name': 'Michael Doyle', 'type': 'Savings', 'balance': 2500.50}
}



def get_accounts_list():
    print('\nAccount ID   Account Name       Account Type   Balance')
    print('------------------------------------------------------')
    # This iterates over the dicitonary and displays it on the Screen
    for account_id, account_info in bank_accounts.items():

        # <13, <19 makes sure that the data doesn't overfill into the other displays
        print(f'{account_id:<13}{account_info["name"]:<19}{account_info["type"]:<13}€{account_info["balance"]:.2f}')

def create_account():
    name = input("Enter Account Holders Name: ")
    account_type = input("Account Type (Savings/Checking/Business: ")
    initial_balance = float(input("Initial Deposit Amount: €"))
    # shows the keys and gets the max of the keys then increments 1 making the ID unique
    account_id = max(bank_accounts.keys()) + 1
    bank_accounts[account_id] = {"name": name, "type": account_type, "balance": initial_balance}
    print(f"Account created succesfully! Account ID: {account_id}")


def check_balance():
    account_id = int(input("Enter the Account ID to check the balance: "))
    # Gets every associated with entered key
    account_info = bank_accounts.get(account_id)
    if account_info:
        print(f"Account Balance: €{account_info['balance']:.2f}")
    else: 
        print("Invalid Account ID.")


def deposit_funds():
    account_id = int(input("Enter the Account ID to deposit funds: "))
    account_info = bank_accounts.get(account_id)
    if account_id:
        amount = float(input("Enter the amount to deposit: €"))
        account_info["balance"] += amount
        print(f"Deposit Successful! New Balance: #{account_info['balance']}")
    else: 
        print("Invalid Account ID.")

def withdraw_funds():
    account_id = int(input("Enter the Account ID to withdraw funds: "))
    account_info = bank_accounts.get[account_id]
    if account_info:
        amount = float(input("How much would you like to deposit"))
        if account_info['balance'] >= amount:
            account_info['balance'] -= amount
            print(f"Withdrawel successful! New Balance: €{account_info['balance']}")
        else:
            print("Insufficient Funds. ")
    else:
        print("Invalid ID. ")
 

def main_menu():
    while True:
        print("\nWelcome to the Banking App!")
        print("1. Get List of Bank Accounts")
        print("2. Create New Account")
        print("3. Check Account Balance")
        print("4. Deposit Funds")
        print("5. Withdraw Funds")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            get_accounts_list()
        elif choice == '2':
            create_account()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            deposit_funds()
        elif choice == '5':
            withdraw_funds()
        elif choice == '6':
            print("You have exited the Bank. Goodbye!")
            quit()
        else: 
            print("You have entered an Invalid selection")


if __name__ == "__main__":
    main_menu()





    




 