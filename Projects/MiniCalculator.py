"""
Mini Calculator
---------------
Performs basic arithmetic operations: +, -, *, /, **

Author: Githubcoderz
"""

def calculator():
    print(" Mini Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponent (**)")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (0-5): ")

        if choice == "0":
            print(" Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print(" Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print(f" Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f" Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f" Result: {num1} * {num2} = {result}")

            elif choice == "4":
                if num2 == 0:
                    print(" Error: Division by zero!")
                else:
                    result = num1 / num2
                    print(f" Result: {num1} / {num2} = {result}")

            elif choice == "5":
                result = num1 ** num2
                print(f" Result: {num1} ** {num2} = {result}")

        except ValueError:
            print(" Please enter valid numbers!")


if __name__ == "__main__":
    calculator()
