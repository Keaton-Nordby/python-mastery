from bank_accounts import *

John = BankAccount(1000, "John")
Dave = BankAccount(5000, "Dave")


print(John.verify_account())
print(Dave.verify_account())



print(Dave.getBalance())
print(Dave.deposit(500))
print(Dave.getBalance())


print(Dave.withdraw(50000))
print(Dave.withdraw(50))

Dave.transfer(500, John)
print(Dave.getBalance())
print(John.getBalance())