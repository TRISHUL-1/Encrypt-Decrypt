def ceasarEncrypter(plain_text, shift):
    LAST_CHARACTER_CODE = 90
    LENGTH = 26
    FIRST_CHARACTER_CODE = 65
    cipher_text = ""
    for letter in plain_text.upper():
        # converting letter to ASCII anc back
        if letter.isalpha():
            char_code = ord(letter)
            new_code = char_code + shift

            if new_code > LAST_CHARACTER_CODE:
                new_code -= LENGTH
            elif new_code < FIRST_CHARACTER_CODE:
                new_code += LENGTH
            new_char = chr(new_code)
            cipher_text += new_char
        else:
            cipher_text += letter
    
    return cipher_text


plain_text = input("Enter the text to encrypt: ")
key = int(input("Enter the key: "))
encrypted_text = ceasarEncrypter(plain_text, key)

print(f"The Encrypted Text: {encrypted_text}")
