import os
import sys

def locate(c): 
    """
        Gets index of characters in the grid
    """
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(grid):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc


def create_grid(key):
    """
        Function to create a 5x5 grid with for playfair encryption and decryption
    """
    key=key.replace(" ", "")
    key=key.upper()
    li=list()
    
    for c in key: 
        if c not in li:
            #if J, replacing it with I
            if c=='J':
                li.append('I')
            else:
                li.append(c)
    
    flag=0
    for i in range(65,91): 
        if chr(i) not in li:
            if i==73 and chr(74) not in li:
                li.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                li.append(chr(i))
    
    k=0
    print("Required grid :",file=f)
    
    for i in range(0,5): 
        for j in range(0,5):
            grid[i][j]=li[k]
            print(li[k],end='',file=f)
            k+=1
        print("",file=f)

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("playfair_input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx  

def encrypt(plaintext): 
    """
    Funtion to encrypt
    """
    plaintext=plaintext.upper()
    plaintext=plaintext.replace(" ", "")   
    i=0
    #replacing X with the adjacently repeated characters in the plaintext

    for s in range(0,len(plaintext)+1,2):
        if s<len(plaintext)-1:
            if plaintext[s]==plaintext[s+1]:
                plaintext=plaintext[:s+1]+'X'+plaintext[s+1:]
                
    if len(plaintext)%2!=0:
        plaintext=plaintext[:]+'X' #Making even length

    print("Key: ", key, file=f)
    print("Ciphertext:",end=' ',file=f)
    ciphertext = ''
    while i<len(plaintext):
        loc=list()
        loc=locate(plaintext[i])
        loc1=list()
        loc1=locate(plaintext[i+1])
        if loc[1]==loc1[1]:
            ciphertext+=grid[(loc[0]+1)%5][loc[1]]
            ciphertext+=grid[(loc1[0]+1)%5][loc1[1]] 
            print("{}{}".format(grid[(loc[0]+1)%5][loc[1]],grid[(loc1[0]+1)%5][loc1[1]]),end=' ',file=f)
        elif loc[0]==loc1[0]:
            ciphertext+=grid[loc[0]][(loc[1]+1)%5]
            ciphertext+=grid[loc1[0]][(loc1[1]+1)%5]
            print("{}{}".format(grid[loc[0]][(loc[1]+1)%5],grid[loc1[0]][(loc1[1]+1)%5]),end=' ',file=f)  
        else:
            ciphertext+=grid[loc[0]][loc1[1]]
            ciphertext+=grid[loc1[0]][loc[1]]
            print("{}{}".format(grid[loc[0]][loc1[1]],grid[loc1[0]][loc[1]]),end=' ',file=f)    
        i=i+2    
    return ciphertext
 
def decrypt(ciphertext):  
    """
        Function to decrypt
    """
    ciphertext=ciphertext.upper()
    
    ciphertext=ciphertext.replace(" ", "")
    
    print("\nDecrypted text: ", text, end=' ',file=f)
    i=0
    sys.stdout = open(os.devnull, 'w')
    while i<len(ciphertext):
        loc=list()
        loc=locate(ciphertext[i])
        loc1=list()
        loc1=locate(ciphertext[i+1])
        if loc[1]==loc1[1]:
            grid[(loc[0]-1)%5][loc[1]] + grid[(loc1[0]-1)%5][loc1[1]]
        elif loc[0]==loc1[0]:
            grid[loc[0]][(loc[1]-1)%5] + grid[loc1[0]][(loc1[1]-1)%5]
        else:
            grid[loc[0]][loc1[1]] + grid[loc1[0]][loc[1]]  
        i=i+2 
    sys.stdout = sys.__stdout__

#Inputs
text, key = read_input()
f = open("playfair_output.txt", "w")
grid=[[0 for i in range(5)] for j in range(5)] 

#Calculations and output
print('\n#====== Playfair Cipher ======#', file=f)
create_grid(key)
ciphertext = encrypt(text)
decrypt(ciphertext)
print('\n#----------------------------#', file=f)