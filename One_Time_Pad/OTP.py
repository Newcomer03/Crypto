"""

Q1: Encryption and Decryption using One Time Pad cipher.

"""
import math, random
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("1_input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx  

def genKey(n):
	out = ""
	for i in range(n):
		out += alphabet[math.floor(random.randint(0, 25))]
	return out

def encrypt(st, key):
	nText = []
	kText = []
	for i in range(len(st)):
		nText.append(alphabet.index(st[i].lower()))
		kText.append(alphabet.index(key[i].lower()))
	out = ""
	for i in range(len(nText)):
		out += alphabet[(nText[i] + kText[i]) % 26]
	return out

def write_output(x, y, key):
    """
        Output to a file
    """
    f = open("1_output.txt", "w")
    print('\n#====== OTP Cipher ======#', file=f)
    print('Text: ' + x, file=f)
    print('Key: ', key, file=f)
    print('Encrypted: ' + y, file=f)
    print('Decrypted: ' + x, file=f)
    print('#----------------------------#\n',file=f)
    f.close()

    print('\n#====== OTP Cipher ======#')
    print('Text: ' + x)
    print('Key: ', key)
    print('Encrypted: ' + y)
    print('Decrypted: ' + x)
    print('#----------------------------#\n')

def decrypt(st, key):
	nText = []
	kText = []
	for i in range(len(st)):
		nText.append(alphabet.index(st[i].lower()))
		kText.append(alphabet.index(key[i].lower()))
	out = ""
	for i in range(len(nText)):
		op = (nText[i] - kText[i])
		if op < 0:
			x = 26 + op
		else:
			x = op % 26
		out += alphabet[x]
	return out

#_________ Main
inp = read_input()[0]
key = genKey(len(inp))
ecpt = encrypt(inp,key)
dcpt = decrypt(ecpt,key)
write_output(inp, ecpt, key)