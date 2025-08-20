import sys

# Check if exactly 3 arguments are passed (excluding the script name)
if len(sys.argv) != 3:
    print("Error: Please pass exactly three arguments: num1 num2 operation")
    print("Example: python num.py 10 5 plus")
else:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    operation = sys.argv[3]
    try:
        n1 = float(num1)
        n2 = float(num2)
        if operation == "plus":
            result = n1 + n2
        elif operation == "minus":
            result = n1 - n2
        elif operation == "mul":
         result = n1 * n2
        elif operation == "mod":
            result = n1 % n2
        elif operation == "floordiv":
            result = n1 // n2
        elif operation == "div":
            result = n1 / n2
        elif operation == "pow":
           result = n1 ** n2
        else:
            print("Error: Unknown operation.")
            sys.exit(1)
            print("Result:, result")

    except ValueError:
     print("Error: Please provide valid numbers.")
    except ZeroDivisionError:
     print("Error: Cannot divide by zero.")