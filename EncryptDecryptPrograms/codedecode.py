import string

def create_cipher(shift):
    """Create a substitution cipher dictionary with a given shift"""
    alphabets = string.ascii_lowercase
    shifted_alphabet = alphabets[shift:] + alphabets[:shift]
    cipher = str.maketrans(alphabets + alphabets.upper(), shifted_alphabet + shifted_alphabet.upper)
    return cipher

def encode(text, shift):
    """Encode the text using the cipher with the specified shift"""
    cipher = create_cipher(shift)
    return text.translate(cipher)

def decode(text, shift):
    """Decode the text using the cipher with the specified shift"""
    return encode(text, -shift)     # Decoding is the reverse of encoding


if __name__ == "__main__":
    shift_value = 5         # You can change the shift value
    text_to_encode = "Hello, Cryptographers !"

    # Encoding
    encoded_text = encode(text_to_encode, shift_value)
    print(f"Encoded Text: {encoded_text}")

    # Decoding
    decoded_text = decode(encoded_text, shift_value)
    print(f"Decoded Text: {decoded_text}")