from tabulate import tabulate

total_prod = int(input("Enter number of products: "))

products = []
cart_amount = 0

for i in range(total_prod):
    print(f"\nProduct {i + 1}")

    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if product_price <= 0 or quantity <= 0:
        print("Product price and quantity must be greater than zero")
        continue

    amount = product_price * quantity

    products.append([product_name, product_price, quantity, amount])

    cart_amount += amount

premium_user = input("\nAre you a premium member (y/n): ")

if cart_amount >= 10000:
    if premium_user.lower() == "y":
        discount = 0.20
    else:
        discount = 0.15
elif cart_amount >= 5000:
    discount = 0.10
elif cart_amount >= 2000:
    discount = 0.05
else:
    discount = 0

    discount_amount = cart_amount * discount
    discounted_amount = cart_amount - discount_amount

    delivery_charge = 0

if discounted_amount < 2000 and premium_user.lower() == "n":
    delivery_charge = 100

final_amount = discounted_amount + delivery_charge

high_value_products = [p[0] for p in products if p[3] >= 1000]

print("\nSHOPPING BILL")

print(tabulate(
    products,
    headers=["Product", "Price", "Quantity", "Amount"],
    tablefmt="grid"
))

print("\nCart Amount:", cart_amount)
print("Discount Amount (",discount,"%) :" , discount_amount)
print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)
print("Products with Amount >= 1000:", high_value_products)