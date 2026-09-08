import json

def generate_bill():
    bill = {}
    bill["Customer Name"] = input("Enter customer name: ")

    n = int(input("Enter number of items: "))
    items = {}

    print("-" * 40)
    for i in range(n):
        name = input(f"Enter item {i + 1} name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))

        items[name] = {
            "Price": price,
            "Qty": qty,
            "Amount": price * qty
        }
        print("-" * 40)

    gst = float(input("Enter GST %: "))

    subtotal = sum(item["Amount"] for item in items.values())
    gst_amount = subtotal * gst / 100
    total = subtotal + gst_amount

    if total >= 10000:
        reward_percent = 15
    elif total >= 7500:
        reward_percent = 10
    elif total >= 5000:
        reward_percent = 5
    else:
        reward_percent = 0

    reward_amount = total * reward_percent / 100
    final_bill = total - reward_amount

    bill["Items"] = items
    bill["Subtotal"] = round(subtotal, 2)
    bill["GST %"] = gst
    bill["GST Amount"] = round(gst_amount, 2)
    bill["Total Bill"] = round(total, 2)
    bill["Reward %"] = reward_percent
    bill["Reward Amount"] = round(reward_amount, 2)
    bill["Final Bill"] = round(final_bill, 2)

    print("\n========== SHOPPING BILL ==========")
    print("Customer:", bill["Customer Name"])

    print("\nItem\t\tPrice\tQty\tAmount")
    print("-" * 40)

    for item, details in bill["Items"].items():
        print(
            f"{item}\t\t{details['Price']}\t{details['Qty']}\t{details['Amount']}"
        )

    print("-" * 40)
    print("Subtotal      :", bill["Subtotal"])
    print("GST Amount    :", bill["GST Amount"])
    print("Total Bill    :", bill["Total Bill"])
    print("Reward %      :", bill["Reward %"])
    print("Reward Amount :", bill["Reward Amount"])
    print("Final Bill    :", bill["Final Bill"])

    print(f"\nThank you for shopping with us, {bill['Customer Name']}!")
    print(f"Original Bill Amount : ₹{bill['Total Bill']:.2f}")
    print(f"Reward Discount      : {bill['Reward %']}%")
    print(f"You Saved            : ₹{bill['Reward Amount']:.2f}")
    print(f"Final Bill Amount    : ₹{bill['Final Bill']:.2f}")

    # print("\nJSON OUTPUT")
    # print(json.dumps(bill, indent=4))

generate_bill()