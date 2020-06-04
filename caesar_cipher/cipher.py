import random

# chars = ['0'...'9']
# test_words = 'hello this is a test, where is the food?'

def encrypt(phrase, shift):
    encrypted_key = ""
    for ca in phrase:
       if ca.isalpha():
            shiftPhrase = ord(ca) + shift
            if shiftPhrase > ord('z'):
                shiftPhrase -= 26
            final = chr(shiftPhrase)
            encrypted_key += final
    return encrypted_key

encrypted = encrypt('abc', 27)


def decrypt(key, message):
    message = message.upper()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = " "

    for letter in message: 
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
            
        else:
            result = result + letter
    
    return result

print(decrypt(27, encrypted))