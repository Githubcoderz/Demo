import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Simple command-line calculator.")

# Positional arguments
parser.add_argument('num1', type=float, help="First number")
parser.add_argument('operator', choices=["+", "-", "*", "/", "//", "%", "**"], help="Operator (+, -, *, /, //, %, **)")
parser.add_argument('num2', type=float, help="Second number")

# Parse the arguments
args = parser.parse_args()

# Perform the calculation
if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':
    if args.num2 == 0:
        result = " Error: Division by zero"
    else:
        result = args.num1 / args.num2
elif args.operator == '//':
    if args.num2 == 0:
        result = " Error: Floor division by zero"
    else:
        result = args.num1 // args.num2
elif args.operator == '%':
    if args.num2 == 0:
        result = " Error: Modulo by zero"
    else:
        result = args.num1 % args.num2
elif args.operator == '**':
    result = args.num1 ** args.num2
else:
    result = " Unknown operator"

# Show the result
print(" Result: {result}")