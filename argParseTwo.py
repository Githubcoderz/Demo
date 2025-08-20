import argparse
parse = argparse.ArgumentParser(description='Validating Options')
parse.add_argument('-a', '--add', action='store_true',help='Add numbers')
parse.add_argument('-s', '--sub', action='store_true',help='Sub numbers')
args = parse.parse_args()
 
if args.add: #true or false if option is given or not
    print('Add option Selected')
if args.sub:
    print('Sub option Selected')
 