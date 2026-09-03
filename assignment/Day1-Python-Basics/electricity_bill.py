print("===== Electricity Bill Calculator =====")

customer_name = input("Enter customer name: ")

previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))

if current_reading < previous_reading:
    print("Error: Current reading cannot be less than previous reading.")
else:
    customer_type = input("Enter customer type (Residential/Commercial): ").lower()

    if customer_type not in ["residential", "commercial"]:
        print("Error: Invalid customer type.")
    else:
        units = current_reading - previous_reading

        # Bill calculation
        if customer_type == "residential":
            fixed_charge = 100

            if units <= 100:
                bill_amount = units * 3
            elif units <= 300:
                bill_amount = (100 * 3) + ((units - 100) * 5)
            else:
                bill_amount = (100 * 3) + (200 * 5) + ((units - 300) * 8)

        else:  # Commercial
            fixed_charge = 250

            if units <= 100:
                bill_amount = units * 5
            elif units <= 300:
                bill_amount = (100 * 5) + ((units - 100) * 8)
            else:
                bill_amount = (100 * 5) + (200 * 8) + ((units - 300) * 12)

        subtotal = bill_amount + fixed_charge

        surcharge = 0
        if subtotal > 2000:
            surcharge = subtotal * 0.05

        total_bill = subtotal + surcharge

        print("\n===== Electricity Bill =====")
        print("Customer Name :", customer_name)
        print("Customer Type :", customer_type.title())
        print("Units Consumed:", units)
        print("Energy Charge : ₹", round(bill_amount, 2))
        print("Fixed Charge  : ₹", fixed_charge)
        print("Surcharge     : ₹", round(surcharge, 2))
        print("Total Bill    : ₹", round(total_bill, 2))