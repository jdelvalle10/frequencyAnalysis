def read_file(ciphered):
    with open(ciphered, 'r', ) as file:
            ciphered_text = file.read()
    return ciphered_text


