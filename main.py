from Cryptofun import hex2b64, b642hex

hexstring = """49276d206b696c6c696e6720796f757220627261
696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"""
hexstring = hexstring.replace("\n", "")
b64string = hex2b64(hexstring)

if hexstring == b642hex(b64string):
    print("okidoki")