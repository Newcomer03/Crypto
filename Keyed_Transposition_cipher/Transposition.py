"""

Q3: Encryption and Decryption using keyed transposition cipher.

"""
import math

key = [3,1,4,5,2]

def read_input():    
    """
        Reading input from files
    """
    tx = []
    with open("2_input.txt", "r") as file: 
        data = file.readlines() 
        for line in data:
            tx.append(line.strip())
    return tx 

def encryptMessage(msg):
    cipher = ""

    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)

    col = len(key)

    row = int(math.ceil(msg_len / col))

    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key[k_indx]-1
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def write_output(x, y, key):
    """
        Output to a file
    """
    f = open("3_output.txt", "w")
    print('\n#====== Keyed Transposition Cipher ======#', file=f)
    print('Text: ' + x, file=f)
    print('Key: ', key, file=f)
    print('Encrypted: ' + y, file=f)
    print('Decrypted: ' + x, file=f)
    print('#------------------------------------------#\n',file=f)
    f.close()

    print('\n#====== Keyed Transposition Cipher ======#')
    print('Text: ' + x)
    print('Key: ', key)
    print('Encrypted: ' + y)
    print('Decrypted: ' + x)
    print('#------------------------------------------#\n')

def decryptMessage(cipher):
    msg = ""

    k_indx = 0

    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    col = len(key)

    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(key))

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key[k_indx]-1

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg

# ______ Main
msg = read_input()[0]
cipher = encryptMessage(msg)
write_output(msg, cipher, key)