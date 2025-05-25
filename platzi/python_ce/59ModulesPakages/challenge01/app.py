import reports
import balance

balances = [['Enero', 1000, 3000], ['Febrero', 5000, 6000], ['Marzo', 5000, 3000], ['Abril', 6000, 3000]]

for month in balances:
    print("______________________________________________________________")
    print(f"REPORTES {month[0]}")
    print(reports.generate_sales_report(month[0], month[1]))
    print(reports.generate_expenses_report(month[0], month[2]))
    print("")
    print("Analisis de balance d ela empresa")
    print("")
    print(f"el balance del mes {month[0]} es ....")
    print(f"{'POSITIVO' if balance.is_balance_positive(month[1], month[2]) else 'NEGATIVO'}")
    print("______________________________________________________________\n")
