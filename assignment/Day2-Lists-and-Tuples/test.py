from tabulate import tabulate

services = {
    1: {"Service": "New Aadhaar Enrollment", "Fee": 1000},
    2: {"Service": "Aadhaar Address Update", "Fee": 300},
    3: {"Service": "Mobile Number Update", "Fee": 200},
    4: {"Service": "Date of Birth Correction", "Fee": 500}
}

request_count = int(input("Enter number of citizen requests: "))

requests = []

for i in range(request_count):
    print(f"\nRequest {i + 1}")

    name = input("Citizen Name: ")

    while True:
        age = int(input("Citizen Age: "))
        if age > 0:
            break
        print("Age must be greater than 0")

    print("\nAvailable Services")
    for key, value in services.items():
        print(f"{key}. {value['Service']} - ₹{value['Fee']}")

    while True:
        choice = int(input("Select Service (1-4): "))
        if choice in services:
            service = services[choice]["Service"]
            fee = services[choice]["Fee"]
            break
        print("Invalid Service Selection")

    if age < 18:
        category = "Minor"
        priority = "Assisted Service"
    elif age < 60:
        category = "Adult"
        priority = "Normal Priority"
    else:
        category = "Senior Citizen"
        priority = "High Priority"

    requests.append(
        [name, age, service, fee, category, priority]
    )

total_requests = len(requests)
total_fees = sum(row[3] for row in requests)
average_fee = total_fees / total_requests if total_requests else 0

fees_above_500 = [row for row in requests if row[3] > 500]

address_updates = [
    row for row in requests
    if row[2] == "Aadhaar Address Update"
]

discounted_fees = [
    [row[0], row[2], round(row[3] * 0.95, 2)]
    for row in requests
]

service_counts = {}

for row in requests:
    service = row[2]
    service_counts[service] = service_counts.get(service, 0) + 1

print("\nAADHAAR SERVICE REPORT")

print("\nCitizen Requests")
print(tabulate(
    requests,
    headers=["Name", "Age", "Service", "Fee", "Category", "Priority"],
    tablefmt="grid"
))

print("\nSummary")
print("Total Requests :", total_requests)
print("Total Fees Collected :", total_fees)
print("Average Fee :", round(average_fee, 2))

print("\nRequests With Fee Above ₹500")
print(tabulate(
    fees_above_500,
    headers=["Name", "Age", "Service", "Fee", "Category", "Priority"],
    tablefmt="grid"
))

print("\nAddress Update Requests")
print(tabulate(
    address_updates,
    headers=["Name", "Age", "Service", "Fee", "Category", "Priority"],
    tablefmt="grid"
))

print("\nFees After 5% Government Discount")
print(tabulate(
    discounted_fees,
    headers=["Name", "Service", "Discounted Fee"],
    tablefmt="grid"
))

count_table = [[service, count] for service, count in service_counts.items()]

print("\nService-wise Request Counts")
print(tabulate(
    count_table,
    headers=["Service", "Count"],
    tablefmt="grid"
))

"""
Assignment: Government Aadhaar Service Request Management System

Business Scenario:
A Government Aadhaar Seva Kendra receives multiple citizen service requests every day.
Citizens can request services such as:

1. New Aadhaar Enrollment
2. Aadhaar Address Update
3. Mobile Number Update
4. Date of Birth Correction
5. Biometric Update

The system must store all citizen requests, calculate service statistics,
identify high-priority requests, and generate a daily service report.

Problem Statement:
Create a Python program to manage and analyze Aadhaar service requests
received by an Aadhaar Seva Kendra.

Requirements:

1. Create a dictionary to store Aadhaar services along with their service fees.

2. Ask the user to enter the number of citizen requests.

3. For every request, accept:
   - Citizen Name
   - Service Choice
   - Citizen Age

4. Validate the input:
   - Citizen age must be greater than zero.
   - Service selection must be valid.

5. Automatically fetch the service fee from the service dictionary.

6. Store every valid request in a list.

7. Calculate:
   - Total requests received
   - Total service fees collected
   - Average service fee

8. Categorize citizens based on age:
   - Below 18      -> Minor
   - 18 to 59      -> Adult
   - 60 and above  -> Senior Citizen

9. Assign priority:
   - Senior Citizen -> High Priority
   - Adult          -> Normal Priority
   - Minor          -> Assisted Service

10. Use list comprehensions to identify:
    - Requests with fees above ₹500
    - Address Update requests
    - Service fees after applying a 5% Government discount

11. Use loops to calculate service-wise request counts.

12. Display the complete Aadhaar Service Report using the
    'tabulate' library with the following details:

    - Citizen Name
    - Age
    - Service Type
    - Service Fee
    - Category
    - Priority

13. Display:
    - Total Requests
    - Total Fees Collected
    - Average Fee
    - Requests with Fee Above ₹500
    - Address Update Requests
    - Discounted Service Fees
    - Service-wise Request Counts

Sample Output:

Enrollment Requests      = 10
Address Update Requests  = 5
Biometric Updates        = 8

Generate a neat and formatted Aadhaar Service Report using tabulate.
"""