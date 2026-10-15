def process_withdraw(balance, amount):
    if amount <= 0:
        return("error: withdraw amount must be positive")
    elif amount > balance:
        return("error: insufficient funds")
    else:
        return"your remaining balance is", balance - amount
print_process = process_withdraw(100, 50)
print(print_process)
