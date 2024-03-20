def getBitValue(n, bitn):
    target_bit = 0x1 << bitn
    return 1 if (n & target_bit) != 0 else 0
def setBitValue(n, bitn):
    target_bit = 0x1 << bitn
    return n | target_bit
def resetBitValue(n, bitn):
    target_bit = ~(0x1 << bitn)
    return n & target_bit