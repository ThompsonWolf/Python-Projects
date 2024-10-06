"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:
Description:
======================================================================================================================
[!]:

"""
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def crack_password(hash_to_crack, wordlist_file):
    with open(wordlist_file, 'r') as file:
        for word in file:
            word = word.strip()
            if hash_password(word) == hash_to_crack:
                print(f"Password found: {word}")
                return
            print("Password not found in wordlist.")


if __name__ == "__main__":
    # The hash of the target password 'letmein'
    target_hash = '2c6ee24b09816a6f14f95d1698b24ead0b6f1b3a3b8a0a1b1b5e6b5e5d5e5d5e'
    # Path to the wordlist file
    wordlist_file = '../wordlist.txt'
    crack_password(target_hash, wordlist_file)
