import hashlib

def crack_hashes(hash_list, wordlist):
    cracked = {}
    for word in wordlist:
        word = word.strip()
        for hash_value in hash_list:
            if hashlib.md5(word.encode()).hexdigest() == hash_value:
                cracked[hash_value] = word
            elif hashlib.sha1(word.encode()).hexdigest() == hash_value:
                cracked[hash_value] = word
            elif hashlib.sha256(word.encode()).hexdigest() == hash_value:
                cracked[hash_value] = word
    return cracked

if __name__ == "__main__":
    # Example hash list and wordlist
    hashes = ["48bb6e862e54f2a795ffc4e541caed4d", "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"]
    wordlist = ["hello", "world", "password", "123456"]

    cracked_hashes = crack_hashes(hashes, wordlist)
    for hash_value, word in cracked_hashes.items():
        print(f"Hash: {hash_value} -> Password: {word}")
