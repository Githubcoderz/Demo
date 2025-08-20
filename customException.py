class InsuffientBalance(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.mesg = f'Trying to withdraw {amount}, balance is {balance}'
        super().__init__(self.mesg)
 
def withdraw(balance, amount):
    if amount > balance:
        raise InsuffientBalance(balance, amount)    
    return balance - amount
 
if __name__ == '__main__':
    balance, amount = 100000, 15000
    try:
        print(f'Balance: {withdraw(balance, amount)}')
    except InsuffientBalance as e:
        print(f'Exception occurrs: {e}')
 
 