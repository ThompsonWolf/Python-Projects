import hashlib
import argparse

# Function to compute the hash based on the specified algorithm
def hash_function(algo, word):
    if algo == 'md5':
        return hashlib.md5(word.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(word.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(word.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algo}")

# Function to crack the hash
def crack_hash(algo, hash_value, wordlist):
    try:
        with open(wordlist, 'r') as f:
            for word in f:
                word = word.strip()
                hashed_word = hash_function(algo, word)
                if hashed_word == hash_value:
                    print(f"[+] Hash cracked! The word is: {word}")
                    return word
        print("[-] Hash not found in wordlist.")
        return None
    except FileNotFoundError:
        print(f"[-] Wordlist file '{wordlist}' not found.")
        return None

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="A simple hash cracking tool.")
    parser.add_argument("hash", help="The hash value to crack.")
    parser.add_argument("wordlist", help="The path to the wordlist file.")
    parser.add_argument("-a", "--algorithm", default="md5", choices=['md5', 'sha1', 'sha256'],
                        help="The hashing algorithm to use (default: md5).")

    args = parser.parse_args()

    print(f"[*] Trying to crack hash: {args.hash}")
    print(f"[*] Using wordlist: {args.wordlist}")
    print(f"[*] Using algorithm: {args.algorithm}")

    crack_hash(args.algorithm, args.hash, args.wordlist)

if __name__ == "__main__":
    main()
