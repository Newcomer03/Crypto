import binascii 

# Get key
def rand_key(p): 
	import random 
	key1 = "" 
	p = int(p) 
	for i in range(p): 
		temp = random.randint(0,1) 
		temp = str(temp) 
		key1 = key1 + temp 
	return(key1) 

# Bit XOR
def xor_b(a,b): 
	temp = "" 
	for i in range(n): 
		if (a[i] == b[i]): 
			temp += "0"
		else: 
			temp += "1"
	return temp 

def write_output(x, y):
    """
        Output to a file
    """
    f = open("feistel_output.txt", "w")
    print('\n#====== Feistel Cipher ======#', file=f)
    print('Text: ' + y, file=f)
    print('Encrypted: ' + x, file=f)
    print('Decrypted: ' + y, file=f)
    print('#----------------------------#\n',file=f)
    f.close()

    print('\n#====== Feistel Cipher ======#')
    print('Text: ' + y)
    print('Encrypted: ' + x)
    print('Decrypted: ' + y)
    print('#----------------------------#\n')

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx  

plaintext = read_input()[0]
PT_Ascii = [ord(x) for x in plaintext] 

# ASCII to 8-bit binary format 
PT_Bin = [format(y,'08b') for y in PT_Ascii] 
PT_Bin = "".join(PT_Bin) 
n = int(len(PT_Bin)//2) 
L1 = PT_Bin[0:n] 
R1 = PT_Bin[n::] 
m = len(R1) 

# Generate Key K1 for the first round 
K1= rand_key(m) 

# Generate Key K2 for the second round 
K2= rand_key(m) 
f1 = xor_b(R1,K1)
R2= xor_b(f1,L1) 
L2 = R1 
f2 = xor_b(R2,K2)
R3 = xor_b(f2,L2)
L3 = R2 

# Cipher text 
bin_data = L3 + R3 
str_data =' '

for i in range(0, len(bin_data), 7): 
	temp_data = bin_data[i:i + 7] 
	decimal_data =  int(temp_data, 2) 
	str_data = str_data + chr(decimal_data) 

# Decryption 
L4 = L3 
R4 = R3 
f3 = xor_b(L4,K2) 
L5 = xor_b(R4,f3) 
R5 = L4 
f4 = xor_b(L5,K1) 
L6 = xor_b(R5,f4) 
R6 = L5 
PT1 = L6+R6 
PT1 = int(PT1, 2) 
RPT = binascii.unhexlify( '%x'% PT1) 

#Outputs
write_output(str_data, plaintext)
