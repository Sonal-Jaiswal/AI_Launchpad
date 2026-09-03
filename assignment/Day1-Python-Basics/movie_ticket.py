# Assignment 5: Movie Ticket Booking System
 
# Create a Python program for a movie ticket booking system.
 
# Requirements - 
# Accept customer name, age, number of tickets, show type, and membership status.
# Show type must be:
# morning
# afternoon
# evening
# Ticket rates:
# Morning: ₹150
# Afternoon: ₹200
# Evening: ₹250
# Provide a 20% child discount if age is below 12.
# Provide a 25% senior citizen discount if age is 60 or above.
# Provide a 10% membership discount if the customer is a member.
# Only one age-based discount can apply.
# Membership discount can be combined with an age-based discount.
# Add a convenience fee of ₹20 per ticket for online bookings.
# Maximum 10 tickets can be booked in one transaction.
# Display the complete booking summary.


print("===== Movie Ticket Booking System =====")

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))

if tickets > 10:
    print("Error: Maximum 10 tickets can be booked in one transaction.")
else:
    show_type = input("Enter show type (morning/afternoon/evening): ").lower()

    if show_type not in ["morning", "afternoon", "evening"]:
        print("Error: Invalid show type.")
    else:
        membership = input("Are you a member? (yes/no): ").lower()

        # Ticket rates
        if show_type == "morning":
            rate = 150
        elif show_type == "afternoon":
            rate = 200
        else:
            rate = 250

        base_amount = rate * tickets

        # Age discount
        age_discount_percent = 0

        if age < 12:
            age_discount_percent = 20
        elif age >= 60:
            age_discount_percent = 25

        age_discount = base_amount * age_discount_percent / 100

        amount_after_age_discount = base_amount - age_discount

        # Membership discount
        membership_discount = 0

        if membership == "yes":
            membership_discount = amount_after_age_discount * 0.10

        subtotal = amount_after_age_discount - membership_discount

        # Online convenience fee
        convenience_fee = tickets * 20

        final_amount = subtotal + convenience_fee

        print("\n===== Booking Summary =====")
        print("Customer Name       :", customer_name)
        print("Age                 :", age)
        print("Show Type           :", show_type.title())
        print("Tickets Booked      :", tickets)
        print("Ticket Rate         : ₹", rate)
        print("Base Amount         : ₹", round(base_amount, 2))
        print("Age Discount        : ₹", round(age_discount, 2))
        print("Membership Discount : ₹", round(membership_discount, 2))
        print("Convenience Fee     : ₹", convenience_fee)
        print("Final Amount        : ₹", round(final_amount, 2))