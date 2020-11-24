key = 'abcdefghijklmnopqrstuvwxyz'

def ceaser_encrypt(n, plaintext):
    """Performs ceaser encryption using the offset"""
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def ceaser_decrypt(n, ciphertext):
    """Performs decryption on the ciphertext and returns plain text"""
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

def xor_encrypt(value):
    """XOR encryption with 127"""
    key = 127
    cipher = []

    for i in value:
        cipher.append(chr(ord(i) ^ key))

    return ''.join(cipher) 

# Decrypt function
def xor_decrypt(cipher):
    """XOR decryption with 127"""
    key = 127
    value = []

    for i in cipher:
        value.append(chr(ord(i) ^ key))

    return ''.join(value)  

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("Ashwin.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line)
    return tx

def xor_write_output(x,y):
    f = open("Sekhari.txt", "w")
    print("____Question 1: XOR encryption with 127 ____\n")
    f.write("____Question 1: XOR encryption with 127 ____\n")
    print("Encrypted: {}\nDecrypted: {}".format(x, y))
    f.write("Encrypted: {}\nDecrypted: {}".format(x, y))
    f.write("\n")
    f.close()

def ceaser_write_output(encoded):
    f = open("Sekhari.txt", "a")
    print("____Question 2: Ceaser encryption____\n")
    f.write("____Question 2: Ceaser encryption____\n")
    print("Offset: {}\nEncrypted: {}\nDecrypted: {}".format(7,encoded, ceaser_decrypt(7, encoded)))
    f.write("Offset: {}\nEncrypted: {}\nDecrypted: {}".format(7,encoded, ceaser_decrypt(7, encoded)))
    f.close()

text1,text2 = read_input()
x = xor_encrypt(text1)
y = xor_decrypt(x)
xor_write_output(x,y)

offset = 7
encrypted = ceaser_encrypt(offset, text2)
ceaser_write_output(encrypted)