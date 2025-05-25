from reports import generate_sales_report, generate_expenses_report

sales_report = generate_sales_report('Octubre', 10000)
expense_report = generate_expenses_report('Octubre', 5000)

print(sales_report)
print(expense_report)