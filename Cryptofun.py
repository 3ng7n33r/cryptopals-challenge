from base64 import b64encode, b64decode

def hex2b64 (hstr):
    return b64encode(bytes.fromhex(hstr)).decode()

def b642hex (b64str):
    return b64decode(b64str.encode()).hex()

def hexXor (hex1, hex2):
    
"""        def hextobin(self, hexval):
        '''
        Takes a string representation of hex data with
        arbitrary length and converts to string representation
        of binary.  Includes padding 0s
        '''
        thelen = len(hexval)*4
        binval = bin(int(hexval, 16))[2:]
        while ((len(binval)) < thelen):
            binval = '0' + binval
        return binval"""

