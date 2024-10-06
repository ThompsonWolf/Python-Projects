"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:                        -
Description:                    Basic Cryptography Script
======================================================================================================================
[!]: This is my basic cryptographic script in python and critically learning how it works

"""
def encrypt(message, key):
    encrypted_message = ""
    for ch in message:
        if ch.isalpha():
            shift = ord('a') if ch.islower() else ord('A')
            encrypted_message += chr((ord(ch) - shift + key) % 26 + shift)
        else:
            encrypted_message += ch
    return encrypted_message

def decrypt(message, key):
    return encrypt(message, -key)

message = input("Enter a message to encrypt: ")
key = int(input("Enter key: "))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

