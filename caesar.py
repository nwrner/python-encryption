
english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]


def encrypt_file_from(path_to_file, given_file_key):
    with open(path_to_file, "r") as in_file:
        file_contents = in_file.readlines()
    with open(path_to_file+".enc", "w") as out_file:

        for line in file_contents:
            enc_line = encrypt_message_from(line, given_file_key)
            if "\n" not in enc_line:
                out_file.write(enc_line+"\n")
            else:
                out_file.write(enc_line)

    print("Completed. Wrote: " + path_to_file+".enc")


def decrypt_file_from(path_to_file, given_file_key):
    with open(path_to_file, "r") as in_file:
        file_contents = in_file.readlines()
    with open(path_to_file+".de_enc", "w") as out_file:

        for line in file_contents:
            unenc_line = decrypt_message_from(line, given_file_key)
            if "\n" not in unenc_line:
                out_file.write(unenc_line+"\n")
            else:
                out_file.write(unenc_line)

    print("Completed. Wrote: " + path_to_file+".de_enc")


def encrypt_message_from(given_message, given_key):
    if given_key > len(english_alphabet):
        raise Exception("Cannot accept key greater than 26! (Sorry I'm new to this.)")

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
