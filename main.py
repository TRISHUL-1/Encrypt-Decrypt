import random
import string

chars = " " + string.punctuation + string.digits +string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

#Encrypt

user_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in user_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"The Encrypted text is: {cipher_text}")


# Decrypt

cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"The Decrypted text is: {plain_text}")
