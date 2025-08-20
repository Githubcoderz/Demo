def bitState(num, pos):
    '''
    Check if the bit at position pos is 0 or 1.
    '''
    return (num >> pos) & 1

def bitToggle(num, pos):
    '''
    Toggle (flip) the bit at position pos.
    '''
    return num ^ (1 << pos)

def nibbleToggle(num, pos):
    '''
    Toggle the nibble (4 bits) starting from bit position pos.
    '''
    return num ^ (0b1111 << pos)

def leftRotate(num, nbits):
    '''
    Left rotate an 8-bit number by nbits bits.
    '''
    nbits = nbits % 8
    return ((num << nbits) | (num >> (8 - nbits))) & 0xFF

def rightRotate(num, nbits):
    '''
    Right rotate an 8-bit number by nbits bits.
    '''
    nbits = nbits % 8
    return ((num >> nbits) | (num << (8 - nbits))) & 0xFF

num = 10   

print("bitState(10, 1):", bitState(num, 1))  
print("bitToggle(10, 1):", bitToggle(num, 1))    
print("nibbleToggle(240, 0):", nibbleToggle(240, 0)) 
print("leftRotate(200, 2):", leftRotate(200, 2)) 
print("rightRotate(200, 2):", rightRotate(200, 2)) 