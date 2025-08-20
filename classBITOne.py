class BitOps:
    def __init__(self, num, pos):
        self.num = num  # Integer value
        self.pos = pos  # Bit position

    def __str__(self):
        return f"Number: {self.num} (Binary: {bin(self.num)}), Position: {self.pos}"

    def bitState(self):
        """Returns 1 if bit at pos is set, else 0"""
        return (self.num >> self.pos) & 1

    def bitToggle(self):
        """Toggles the bit at pos"""
        self.num ^= (1 << self.pos)

    def nibbleToggle(self):
        """Toggles 4 bits (a nibble) starting at the given position"""
        self.num ^= (0b1111 << self.pos)

# Create an object
b = BitOps(29, 3)
print(b)          
b.bitState()        
b.bitToggle()       
b.nibbleToggle()    