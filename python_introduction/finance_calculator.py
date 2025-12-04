# Prompt the user for their monthly income: “Enter your monthly income: ”
monthly_income = float(input("Enter your monthly income: "))
# Prompt the user for their monthly expenses: “Enter your monthly expenses: ”
monthly_expenses = float(input("Enter your monthly expenses: "))
# Calculate the monthly savings as income minus expenses.
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")

# anual interest rate
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")