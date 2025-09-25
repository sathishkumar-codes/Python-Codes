correct_pin = "2003"
balance = 5000  # Initial balance
attempts = 0
max_attempts = 3

while True:
    pin = input("Enter ATM PIN (or type 'exit' to quit): ")

    if pin.lower() == "exit":
        print("Exiting... Thank you!")
        break

    if pin == correct_pin:
        print("PIN accepted. Welcome!\n")

        # Menu loop
        while True:
            print("\n----- ATM Menu -----")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print(f"Your balance is ₹{balance}")
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                balance += amount
                print(f"₹{amount} deposited. New balance: ₹{balance}")
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print(f"₹{amount} withdrawn. New balance: ₹{balance}")
                else:
                    print("Insufficient balance!")
            elif choice == "4":
                print("Thank you! Have a nice day.")
                break
            else:
                print("Invalid choice, try again.")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Try again...\n")
        if attempts >= max_attempts:
            print("Too many incorrect attempts. Card blocked!")
            break