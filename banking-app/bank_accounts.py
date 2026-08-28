class BalanceException(Exception):
    pass




class BankAccount:
    """ Initial creation of bank account """
    def __init__(self, initial_amount, acctName):
        self.balance = initial_amount
        self.name = acctName
        
        
    def verify_account(self):
        return f"Account '{self.name}' has been successfully created."

        
    """ Return current balance """
    def getBalance(self):
        return f"\nAccount '{self.name}' balance = ${self.balance:.2f}"
        
        
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be greater than 0"
        else:
            self.balance += amount
            return f"Deposit successful. {self.name}'s new balance is {self.balance}"
        
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
     
        raise BalanceException(
            f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
        )
            
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            return f"Withdraw successful. {self.name}'s new balance is ${self.balance:.2f}"
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
        