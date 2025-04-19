import statistics
import csv

monthly_sales = {}
with open('monthly_sales.csv', mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#hallar la mediana
mean_sales = statistics.median(sales)
print(f"La mediana es: {mean_sales}")

#hallar la moda
mean_sales = statistics.mode(sales)
print(f"La moda es: {mean_sales}")

#hallar la desviacion standar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

#hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza: {variance_sales}")

#hallar maximo y minimo
max_sale = max(sales)
min_sale = min(sales)
range_sales = max_sale - min_sale

print(f"Maximo: {max_sale}, Minimo: {min_sale}", f"Rango de ventas: {range_sales}")

