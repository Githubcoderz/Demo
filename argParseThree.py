import argparse
parse = argparse.ArgumentParser(description='Performing basic Calculation')
parse.add_argument('-a', '--add',nargs=2, type=float ,help='Add numbers')
parse.add_argument('-s', '--sub',nargs=2, type=float,help='Sub numbers')
args = parse.parse_args()
 
if args.add: #true or false if option is given or not
    print(f'Adding {args.add[0]} {args.add[1]} --> res {args.add[0] + args.add[1]}')
if args.sub:
    print(f'Subtracting {args.sub[0]} {args.sub[1]} --> res {args.sub[0] - args.sub[1]}')
