#117CS0263 - Ashwin Sekhari
def write_output(x,y):
    """
    	Output to a file
    """
    f = open("rail_output.txt", "w")
    print('\n#====== Rail Fence Cipher ======#', file=f)
    print('Text: ' + y, file=f)
    print('Encrypted: ' + x, file=f)
    print('Decrypted: ' + y, file=f)
    print('#----------------------------#\n',file=f)
    f.close()

    print('\n#====== Rail Fence Cipher ======#')
    print('Text: ' + y)
    print('Encrypted: ' + x)
    print('Decrypted: ' + y)
    print('#----------------------------#\n')

def encrypt(text, key): 
	"""
		Function to encrypt the plain text
	"""
	rail = [['\n' for i in range(len(text))] for j in range(key)] 
	
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)): 
		if (row == 0) or (row == key - 1): 
			dir_down = not dir_down 
		
		rail[row][col] = text[i] 
		col += 1
		
		if dir_down: 
			row += 1
		else: 
			row -= 1
	 
	result = [] 
	for i in range(key): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("" . join(result)) 
	
def decrypt(cipher, key): 
	"""
		Function to decrypt the plain text
	"""
	rail = [['\n' for i in range(len(cipher))] for j in range(key)] 
	dir_down = None
	row, col = 0, 0
	
	for i in range(len(cipher)): 
		if row == 0: 
			dir_down = True
		if row == key - 1: 
			dir_down = False
		
	
		rail[row][col] = '*'
		col += 1
		
		if dir_down: 
			row += 1
		else: 
			row -= 1
			
	index = 0
	for i in range(key): 
		for j in range(len(cipher)): 
			if ((rail[i][j] == '*') and
			(index < len(cipher))): 
				rail[i][j] = cipher[index] 
				index += 1

	result = [] 
	row, col = 0, 0
	for i in range(len(cipher)): 
		
	
		if row == 0: 
			dir_down = True
		if row == key-1: 
			dir_down = False
			
		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
			
		if dir_down: 
			row += 1
		else: 
			row -= 1
	return("".join(result)) 

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("rail_input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx  

text = read_input()
cipher = encrypt(text, 2)
res = decrypt(cipher, 2)
write_output(res, cipher)
