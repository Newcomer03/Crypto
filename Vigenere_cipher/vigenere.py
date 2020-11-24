def new_alph(ch):
    """
    generates the new alphabet acc to the characters in key
    """
    ch = ch.lower()
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("vigenere_input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx
   
def encrypt(text, big_key):
    """
    Encrypts the given text and converts into cyphertext
    """
    res = ''
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res
    
def decrypt(text, big_key):
    """
    Convert the cypher texts to plain text
    """
    res = ''
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += alph[new.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res    

def write_output(x,y):
    """
    Outputs
    """
    f = open("vigenere_output.txt", "w")
    print('\n#====== Vigenere Cipher ======#', file=f)
    print('Text: ' + text, file=f)
    print('Key: ' + key , file=f)
    print('Encrypted: ' + x, file=f)
    print('Decrypted: ' + text_decrypt, file=f)
    print('#----------------------------#\n',file=f)
    f.close()

    print('\n#====== Vigenere Cipher ======#')
    print('Text: ' + text)
    print('Key: ' + key)
    print('Encrypted: ' + x)
    print('Decrypted: ' + text_decrypt)
    print('#----------------------------#\n')
    
#Taking input,
text, key = read_input()
alph = 'abcdefghijklmnopqrstuvwxyz'

big_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
text_encrypt = encrypt(text, big_key)
text_decrypt = decrypt(text_encrypt, big_key)

write_output(text_encrypt, text_decrypt)
