import random, os, time
from tqdm import tqdm

alphabet_key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 
                'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                'q', 'r', 's', 't', 'u', 'v', 'w', 
                'x', 'y', 'z', ':', ';', '-', '.', 
                ',', '=', '+', '1', '0', '2', '3', 
                '4', '5', '6', '7', '8', '9', '?', 
                '!', '(', ')', '[', ']', '@', '#', 
                '№', '$', '%', '^', '*', '&', '<', 
                '>', '/', '|', '\\', ' ', '"', "'"]

alphabet_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                  'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                  'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 
                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                  'q', 'r', 's', 't', 'u', 'v', 'w', 
                  'x', 'y', 'z', ':', ';', '-', '.', 
                  ',', '=', '+', '1', '0', '2', '3', 
                  '4', '5', '6', '7', '8', '9', '?', 
                  '!', '(', ')', '[', ']', '@', '#', 
                  '№', '$', '%', '^', '*', '&', '<', 
                  '>', '/', '|', '\\', ' ', '"', "'"]


def clear():
    os.system(['clear','cls'][os.name == 'nt'])


def start():
    print('Encrypt or decrypt? (e/d)')
    print('x - for exit.')
    match input('> '):
        case 'd':
            decrypt()
        case 'e':
            encrypt()
        case 'x':
            exit()


def encrypt():
    global alphabet_key, alphabet_value
    print("Input your's text (only english):")
    text = input()
    text = ''.join(list(filter(lambda symbol: symbol in alphabet_key, list(text))))    ## remove all characters outside the alphabet

    key = ''
    print("Input user-key for text:")
    alpha_seed = input("> ")
    key = key + alpha_seed

    ## Alpha-step: shuffle alphabet with symbols, then simple crypting text {'a': 'h'} a --> h
    random.seed(alpha_seed)
    random.shuffle(alphabet_value)
    crypt_dict = dict(zip(alphabet_key, alphabet_value))    ## making substitution cipher dict
    encrypt_alpha = ''
    for i in tqdm(text, desc='Substitution cipher'):
        encrypt_alpha = encrypt_alpha + crypt_dict.get(i)
        time.sleep(0.001)
    
    #print(f'[1]: {encrypt_alpha}')   ## for check

    ## Beta-step: crash crypted text into the pieces!
    encrypt_alpha = encrypt_alpha[::-1]    ## reverse text

    #print(f'[2]: {encrypt_alpha}')   ## for check

    if len(encrypt_alpha)%2 != 0:     ## if it's odd len --> add '~' to the end. It's nessory for further splitting into pairs
        encrypt_alpha = encrypt_alpha + '~'

    #print(f'[3]: {encrypt_alpha}')   ## for check


    ## Beta-step: reversing text and simple shuffle
    encrypt_beta = []
    for i in tqdm(range(len(encrypt_alpha)//2), desc='Splitting'):
        encrypt_beta.append(list(encrypt_alpha[0] + encrypt_alpha[1]))
        encrypt_alpha = encrypt_alpha[2:]

    #print(f'[4]: {encrypt_beta}')   ## for check
    
    encrypt_beta = encrypt_beta[::-1]
    
    #print(f'[5]: {encrypt_beta}')   ## for check

    encrypt_final = ''
    for unit in tqdm(encrypt_beta, desc='Assembly of parts'):
        for symbol in unit:
            encrypt_final = encrypt_final + symbol

    print()
    print(encrypt_final)
    print(f"Key: {key}")
    input('> Enter')
    clear()
    alphabet_value = alphabet_key.copy()


def decrypt():
    global alphabet_key, alphabet_value
    print("Enter crypted text here:")
    crypt_final = input()
    print("Enter key for decrypt:")
    key = input()

    crypt_beta = []
    for i in tqdm(range(len(crypt_final)//2), desc='Splitting'):
        crypt_beta.append(list(crypt_final[0] + crypt_final[1]))
        crypt_final = crypt_final[2:]

    #print(f'[5]: {crypt_beta}')   ## for check

    crypt_beta = crypt_beta[::-1]

    #print(f'[4]: {crypt_beta}')   ## for check

    crypt_alpha = ''
    for unit in tqdm(crypt_beta, desc='Assembly of parts'):
        for symbol in unit:
            crypt_alpha = crypt_alpha + symbol

    #print(f'[3]: {alpha_beta}')   ## for check

    crypt_alpha = crypt_alpha.replace('~', '')

    #print(f'[2]: {crypt_alpha}')   ## for check

    crypt_alpha = crypt_alpha[::-1]

    #print(f'[1]: {crypt_alpha}')   ## for check

    random.seed(key)
    random.shuffle(alphabet_value)
    crypt_dict = dict(zip(alphabet_value, alphabet_key))    ## making substitution cipher dict

    text = ''
    for i in tqdm(crypt_alpha, desc='Transcription'):
        text = text + crypt_dict.get(i)

    print()
    print(text)
    print(f"Key: {key}")
    input('> Enter')
    clear()
    alphabet_value = alphabet_key.copy()
    