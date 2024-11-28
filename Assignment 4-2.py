# Employee Productivity Bonus Calculator

# Get employee information from input
employee_name = input("Employee's name: ")
num_shifts = int(input("Number of Shifts: "))
num_transactions = int(input("Number of transactions: "))
transaction_dollar_value = float(input("Transaction dollar value: "))

# Calculate productivity score
avg_transaction_value = transaction_dollar_value / num_transactions
productivity_score = avg_transaction_value / num_shifts

# Calculate bonus using nested if statement
bonus = 0.0
if productivity_score <= 30:
    bonus = 50.00
elif productivity_score <= 69:
    bonus = 75.00
elif productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Print results
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.2f}")