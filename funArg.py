def funOne(a,b,*c):
    print(f'arg a:{a} b: {b} c:{c}')
    print('*'*40)

if __name__=='__main__':
    funOne(10,20,30,40,50,60,70)
    funOne(10,20,30)
    funOne(10,'hello',123.45)