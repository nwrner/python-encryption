english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
message = "This is a message to be encrypted."
key = 3


def encrypt_message_from(given_message, given_key):
    encrypted_given_message = ""
    for letters in given_message:
        try:
            offset = english_alphabet.index(letters.lower())+given_key
            if offset > len(english_alphabet):
                new_offset = offset-len(english_alphabet)
                if letters.isupper():
                    encrypted_given_message += english_alphabet[new_offset].upper()
                else:
                    encrypted_given_message += english_alphabet[new_offset]
            else:
                encrypted_given_message += english_alphabet[offset]
        except ValueError:
            encrypted_given_message += letters

    return encrypted_given_message


def decrypt_message_from(given_message, given_key):
    clear_text = ""
    for letters in given_message:
        try:
            reverse_offset = english_alphabet.index(letters.lower())-given_key
            if letters.isupper():
                clear_text += english_alphabet[reverse_offset].upper()
            else:
                clear_text += english_alphabet[reverse_offset]
        except ValueError:
            clear_text += letters

    return clear_text


cipher_text = encrypt_message_from(message, key)
clear_text = decrypt_message_from(cipher_text, key)

print(cipher_text)
print(clear_text)
