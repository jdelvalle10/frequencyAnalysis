def read_file(ciphered):
    with open(ciphered, 'r', ) as file:
            ciphered_text = file.read()
    return ciphered_text


def frequencyAnalysis(cipheredText):
    frequency = {}
    for letter in cipheredText:
        frequency[letter] = (cipheredText.count(letter)/len(cipheredText))*100
    return frequency

cipher = read_file('cipherText.txt')
possibleKey = frequencyAnalysis(cipher)


