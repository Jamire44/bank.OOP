import pytest 
from main import get_accounts_list, create_account, check_balance, deposit_funds, withdraw_funds, main_menu

def test_get_accounts_List(capsys):

    bank_accounts = {
        1: {"name": "John Doe", "type": "Savings", "balance": 1000},
        2: {"name": "Jane Smith", "type": "Checking", "balance": 2500},
        3: {"name": "Mike Johnson", "type": "Savings", "balance": 500},
    }

    get_accounts_list(bank_accounts)

    captured = capsys.readouterr()
    
    expected_output = (
        "\nAccount ID   Account Name       Account Type   Balance\n"
        "------------------------------------------------------\n"
        "1            John Doe           Savings       €1000.00\n"
        "2            Jane Smith         Checking      €2500.00\n"
        "3            Mike Johnson       Savings       €500.00\n"
    )

    assert captured.out == expected_output





    

        
