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
    # Gets every 
    account_info = bank_accounts.get(account_id)
    if account_info:
        print(f"Account Balance: €{account_info['balance']:.2f}")
    else: 
        print("Invalid Account ID.")


def main_menu():
    pass


check_balance()
check_balance()
check_balance()



if __name__ == "__main__":
    main_menu()





    




 