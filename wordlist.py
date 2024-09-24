"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:                        Itertools
Description:                    Creating a Wordlist
======================================================================================================================
[!]:

"""
import itertools


def create_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(characters, repeat=length):
                f.write("".join(word) + '\n')


if __name__ == "__main__":
    # Characters to include in the wordlist
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    characters = ascii_uppercase + ascii_lowercase + digits + punctuation

    min_length = 5  # Minimum length of words
    max_length = 5  # Maximum length of words
    output_file = 'wordlist.txt'  # Output file name
    create_wordlist(characters, min_length, max_length, output_file)
    print(f"Wordlist created and saved to {output_file}")
