import argparse

parser = argparse.ArgumentParser(description="Simple argparse example")

# --age argument (expects an integer)
parser.add_argument('--age', type=int, help='Age of the user')

# --show-age flag (boolean flag to decide whether to display age)
parser.add_argument('--show-age', action='store_true', help='Show age if provided')

# --value argument (expects a float)
parser.add_argument('--value', type=float, help='A float value (example: 10.5)')

args = parser.parse_args()

# If --show-age is passed, print the age (if provided)
if args.show_age:
    if args.age is not None:
        print(f" User age: {args.age}")
    else:
        print(" Age not provided.")

# If --value is passed
if args.value is not None:
    print(f" Float value: {args.value}")