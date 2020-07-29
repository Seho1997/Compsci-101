"""
Name: Se Ho Lee
Username: slee626
Student Id: 890218467
Description: A program which simulates four transactions on a bank account.[4 marks]
"""
import random

initial_balance = 786
transaction_minimum = 15
transaction_maximum = 501
initial_balance_title = "Initial bank balance: $"
final_balance_title = "Final bank balance: $"
sum_title = "Sum of transactions: $"
border_line = ("=" * 26)


first_transaction = (random.randrange(15,501) * random.randrange(-1,2,2))
second_transaction = (random.randrange(15,501) * random.randrange(-1,2,2))
third_transaction = (random.randrange(15,501) * random.randrange(-1,2,2))
final_transaction = (random.randrange(15,501) * random.randrange(-1,2,2))
total_transaction = (first_transaction + second_transaction + third_transaction + final_transaction)

first_initial_balance = (initial_balance + first_transaction)
second_initial_balance = (first_initial_balance + second_transaction)
third_initial_balance = (second_initial_balance + third_transaction)
final_balance = (third_initial_balance + final_transaction)

print(initial_balance_title, initial_balance, sep = "")
print(border_line)
print("1: ", first_transaction, " (", first_initial_balance, ")", sep = "")
print("2: ", second_transaction, " (", second_initial_balance, ")", sep = "")
print("3: ", third_transaction, " (", third_initial_balance, ")", sep = "")
print("4: ", final_transaction, " (", final_balance, ")", sep = "")
print(border_line)
print(final_balance_title, final_balance, sep = "")
print(sum_title, total_transaction, sep = "")
print(border_line)
