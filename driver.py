import caesar

enc_text = caesar.encrypt_message_from("encrypt", 3)
print(enc_text)

caesar.encrypt_file_from("test.txt", 6)
caesar.decrypt_file_from("test.txt.enc", 6)
