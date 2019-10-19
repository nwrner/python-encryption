english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
message = "This is a message to be encrypted."
key = 3


message = message.replace(" ","").lower()
encrypted_message = ""
for letters in message:
    try:
        offset = english_alphabet.index(letters)+key
        if offset > len(english_alphabet):
            new_offset = offset-len(english_alphabet)
            encrypted_message += english_alphabet[new_offset]
        else:
            encrypted_message += english_alphabet[offset]
    except ValueError:
        pass

print(encrypted_message)
