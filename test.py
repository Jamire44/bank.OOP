import pytest
from main import BankAccount, SavingsAccount, Bank

def test_bank_account_deposit():
    account = BankAccount("John Doe")
    account.deposit(1000)
    assert account.balance == 1000

def test_bank_account_withdraw():
    account = BankAccount("John Doe")
    account.deposit(1000)
    account.withdraw(500)
    assert account.balance == 500

def test_bank_account_with_insufficient_balance():
    account = BankAccount("Jamie Doyle")
    account.withdraw(100)  # Withdrawal without depositing first
    assert account.balance == 0

def test_is_valid_number_valid():
    assert BankAccount.is_valid_number("100") == True
    assert BankAccount.is_valid_number("12.10") == True
    assert BankAccount.is_valid_number("0") == True

def test_is_valid_number_invalid():
    assert BankAccount.is_valid_number("abc") == False
    assert BankAccount.is_valid_number("12.34.56") == False
    assert BankAccount.is_valid_number("") == False

def test_savings_account_interest():
    account = SavingsAccount("Jamie Doyle", 0.05)
    account.deposit(1000)

    account.interest()

    expected_balance = 1000 + (1000 * 0.05)
    assert account.balance == expected_balance    

if __name__ == "__main__":
    pytest.main()

    

        
