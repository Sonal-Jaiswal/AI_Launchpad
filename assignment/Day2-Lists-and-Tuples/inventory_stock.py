from tabulate import tabulate

n = int(input("Enter number of products: "))

products = []

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    current_stock = int(input("Enter current stock: "))
    minimum_stock = int(input("Enter minimum stock: "))
    print("-----------------------------------------------")

    if price <= 0 or current_stock < 0 or minimum_stock <= 0:
        print("Invalid data")
        continue

    if current_stock == 0:
        status = "Out of Stock"
    elif current_stock < minimum_stock:
        status = "Low Stock"
    elif current_stock == minimum_stock:
        status = "Reorder Recommended"
    else:
        status = "Sufficient Stock"

    if current_stock > minimum_stock:
        reorder_qty = 0
    else:
        reorder_qty = minimum_stock * 2 - current_stock

    inventory_value = price * current_stock

    products.append([
        name, price, current_stock, minimum_stock,
        status, reorder_qty, inventory_value
    ])

out_of_stock = [p[0] for p in products if p[4] == "Out of Stock"]

reorder_products = [p[0] for p in products
                    if p[4] in ["Low Stock", "Reorder Recommended", "Out of Stock"]]

high_value_products = [p[0] for p in products if p[6] > 10000]

print("\nINVENTORY REPORT")

print(tabulate(
    products,
    headers=["Product","Price","Current Stock","Min Stock","Status","Reorder Qty","Inventory Value"],
    tablefmt="grid"
))

print("\nOut of Stock Products:", out_of_stock)
print("Products Requiring Reorder:", reorder_products)
print("Inventory Value > 10000:", high_value_products)