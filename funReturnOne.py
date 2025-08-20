def isPRIME(num):
    res = True
    for i in range (2, num//2+1):
        if num % i ==0:
            res = False
            break
        return
    