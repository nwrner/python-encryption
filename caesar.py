
english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]


def encrypt_message_from(given_message, given_key):
    if given_key > len(english_alphabet):
        raise Exception("Cannot accept key greater than " + str(len(english_alphabet)) + "! (Sorry I'm new to this.)")

    encrypted_given_message = ""
    for letters in given_message:
        try:
            offset = english_alphabet.index(letters.lower())+given_key
            if offset > len(english_alphabet):
                new_offset = offset-len(english_alphabet)
                if letters.isupper():
                    encrypted_given_message += english_alphabet[new_offset].upper()
                if not letters.isupper():
                    encrypted_given_message += english_alphabet[new_offset]
            else:
                if letters.isupper():
                    encrypted_given_message += english_alphabet[offset].upper()
                if not letters.isupper():
                    encrypted_given_message += english_alphabet[offset]

        except ValueError:
            encrypted_given_message += letters

    return encrypted_given_message


def decrypt_message_from(given_message, given_key):
    return_clear_text = ""
    for letters in given_message:
        try:
            reverse_offset = english_alphabet.index(letters.lower())-given_key
            if letters.isupper():
                return_clear_text += english_alphabet[reverse_offset].upper()
            else:
                return_clear_text += english_alphabet[reverse_offset]
        except ValueError:
            return_clear_text += letters

    return return_clear_text




