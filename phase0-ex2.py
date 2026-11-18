def expense_calculator():
    expenses = [
        {'Shopping' : 5000},
        {'Entertainment' : 4500},
        {'Grocery' : 1000},
        {'EMI' : 4500},
    ] 
    values = [list(item.values())[0] for item in expenses] 
    return sum(values) 
 
result = expense_calculator()
print(f"Total expense = {result}")


