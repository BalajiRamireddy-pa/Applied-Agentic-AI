def factorial():
    """
    Calculates the factorial of a non-negative integer using recursion.
    """

    def recursive_fact(number):
        if number == 0 or number == 1:
            return 1
        return number * recursive_fact(number - 1)

    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        print(f"Factorial of {number} is {recursive_fact(number)}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


def sum_numbers():
    """
    Calculates the sum of numbers from 1 to n.
    """

    try:
        number = int(input("Enter a positive integer: "))

        if number < 1:
            print("Please enter a positive integer.")
            return

        total = sum(range(1, number + 1))
        print(f"Sum from 1 to {number} is {total}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


def bmi_calculator():
    """
    Calculates Body Mass Index and displays the BMI category.
    """

    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = weight / (height ** 2)

        print(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def fibonacci():
    """
    Displays Fibonacci series up to n terms.
    """

    try:
        terms = int(input("Enter the number of terms: "))

        if terms <= 0:
            print("Please enter a positive integer.")
            return

        first = 0
        second = 1

        print("Fibonacci Series:")

        for _ in range(terms):
            print(first, end=" ")
            first, second = second, first + second

        print()

    except ValueError:
        print("Invalid input. Please enter an integer.")


def atm_simulation():
    """
    Simulates an ATM with PIN verification.
    """

    correct_pin = "1234"
    balance = 10000
    attempts = 0

    while attempts < 3:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("Login successful.")
            break

        attempts += 1
        print("Incorrect PIN.")

    if attempts == 3:
        print("Too many incorrect attempts.")
        print("Your account has been frozen for 24 hours.")
        return

    while True:
        print("\nATM MENU")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Available Balance: ₹{balance:.2f}")

            elif choice == 2:
                amount = float(input("Enter deposit amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    balance += amount
                    print("Deposit successful.")

            elif choice == 3:
                amount = float(input("Enter withdrawal amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawal successful.")

            elif choice == 4:
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")