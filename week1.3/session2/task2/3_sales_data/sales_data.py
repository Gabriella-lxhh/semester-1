# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
with open("sales.csv", "r") as infile:
    data = infile.readlines()

data = [line.strip().split(",") for line in data[1:]]

if data:
    largest_sale = int(data[0][2])
    largest_day = data[0][0]
    total = 0
    product_units = {}
    
    for row in data:
        sale_amount = int(row[2])
        units_sold = int(row[3])
        product = row[1]

        total += sale_amount

        if sale_amount > largest_sale:
            largest_sale = sale_amount
            largest_day = row[0]

        product_units[product] = product_units.get(product, 0) + units_sold

    average_sale = total / len(data)
    most_sold_widget = max(product_units, key=product_units.get)

    print(f"Largest sale day: {largest_day} with amount: {largest_sale}")
    print(f"Average sale amount: {average_sale}")
    print(f"Most sold widget: {most_sold_widget} with units sold: {product_units[most_sold_widget]}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows