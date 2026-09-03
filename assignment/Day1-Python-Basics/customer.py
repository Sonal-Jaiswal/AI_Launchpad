
# Requirements - 
# Accept customer name, membership status, cart amount, and coupon code.
# Membership status should be yes or no.
# Apply the following discounts:
# Cart amount ₹10,000 or more and member: 20%
# Cart amount ₹10,000 or more and non-member: 15%
# Cart amount ₹5,000 or more: 10%
# Cart amount ₹2,000 or more: 5%
# Below ₹2,000: No discount
# Apply an additional ₹500 discount if coupon code is SAVE500 and the cart amount is at least ₹5,000.
# Delivery is free for members or when the amount after discount is ₹2,000 or more.
# Otherwise, add ₹100 as delivery charges.
# Display the complete bill.

customer_name = input("Enter Customer Name: ")
membership = input("Are you a member? (y/n): ").lower()
cart_amount = float(input("Enter Cart Amount: ₹"))
coupon_code = input("Enter Coupon Code: ")

if cart_amount < 0:
    print("Error: Invalid Cart Amount")

else:
    if cart_amount >= 10000:
        if membership == "y":
            discount = cart_amount * 0.20
        else:
            discount = cart_amount * 0.15

    elif cart_amount >= 5000:
        discount = cart_amount * 0.10

    elif cart_amount >= 2000:
        discount = cart_amount * 0.05

    else:
        discount = 0

    discounted_amount = cart_amount - discount

    coupon_discount = 0
    if coupon_code == "SAVE500" and cart_amount >= 5000:
        coupon_discount = 500

    amount_after_coupon = discounted_amount - coupon_discount

    if membership == "y" or amount_after_coupon >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_bill = amount_after_coupon + delivery_charge

    print("\n--------- SHOPPING BILL ---------")
    print("Customer Name   :", customer_name)
    print("Membership      :", "Yes" if membership == "y" else "No")
    print("Cart Amount     : ₹", cart_amount)
    print("Discount        : ₹", discount)
    print("Coupon Discount : ₹", coupon_discount)
    print("Delivery Charge : ₹", delivery_charge)
    print("---------------------------------")
    print("Final Bill      : ₹", final_bill)
    print("---------------------------------")