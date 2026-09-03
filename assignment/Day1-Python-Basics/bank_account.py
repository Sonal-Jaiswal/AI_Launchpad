Account_Number =12345678
PIN = 1234
balance = 10000
print("--------------------------------------")
Account_Num = int(input("Enter Account Number: "))
if Account_Number == Account_Num:
    
    PIN_ = int(input("Enter PIN: "))

    if PIN == PIN_:
        print("Access Granted")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("--------------------------------------")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            deposit = float(input("Enter Deposit Amount: "))
            print("--------------------------------------")
            if deposit > 0:
                balance = balance + deposit
                print("Deposit Successful")
                print("Available Balance =", balance)
            else:
                print("Invalid Amount")
        elif choice == 2:
            withdraw = float(input("Enter Withdrawal Amount: "))
            print("--------------------------------------")
            if withdraw <= 0:
                print("Invalid Amount")
            elif withdraw > 25000:
                print("Transaction Limit Exceeded")
            elif withdraw > balance:
                print("Insufficient Balance")
            else:
                balance = balance - withdraw
                print("Withdrawal Successful")
                print("Available Balance =", balance)
        elif choice == 3:
            print("Current Balance =", balance)
        else:
            print("Invalid Menu Choice")

    else:
        print("--------------------------------------")
        print("Invalid PIN")

else:
    print("--------------------------------------")
    print("Invalid Account Number")

print("--------------------------------------")