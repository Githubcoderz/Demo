import argparse
import os
from datetime import datetime

def list_files():
    print("\n Files and Directories:")
    os.system('ls')

def show_date():
    today = datetime.now().strftime("%Y-%m-%d")
    print("\n Today's Date:", today)

def encode_string(s):
    # Sample encoding: reverse + uppercase
    encoded = s[::-1].upper()
    print("\n Encoded String:", encoded)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Option-based utility program.")

    parser.add_argument('-1', action='store_true', help='List all files and directories')
    parser.add_argument('-d', action='store_true', help="Display today's date")
    parser.add_argument('-e', metavar='STRING', help='Encode and display the given string')

    args = parser.parse_args()

    if args.__dict__.values().__contains__(True) or args.e:
        if args.__dict__.get('1'):
            list_files()
        if args.d:
            show_date()
        if args.e:
            encode_string(args.e)
    else:
        parser.print_help()