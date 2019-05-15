import csv

with open('yl22_revenue.csv', 'r', newline='') as revenue:
    revenue = csv.DictReader(revenue)
    for lines in revenue:
        print(lines)
with open('yl22_expenses.csv', 'r', newline='') as expenses:
    expenses = csv.DictReader(expenses)
