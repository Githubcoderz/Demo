import sys

# Check if any arguments were passed (excluding the script name)
if len(sys.argv) > 1:
    print("Arguments passed:", sys.argv[1:])
else:
    print("Error: No arguments were passed.")