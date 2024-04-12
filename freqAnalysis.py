# Script that takes a text file and calculates the frequency of each character in the text.

def openfile(cipher):
    file = open(cipher, 'r')
    cipheredtext = file.read()
    file.close()
    return cipheredtext

def uppercasing(cipher):
    cipherUp = ""
    for c in cipher:
        if c.isalpha():
            cipherUp += c.upper()

    return cipherUp

def frequencies(cipheredtext):
    freqDict = {}
    for c in cipheredtext:
        if not c in freqDict.keys():
            freqDict[c] = cipheredtext.count(c)
    return freqDict


a = openfile("text.txt")
b = uppercasing(a)
table = frequencies(b)

for key in table:
    print(f"{key} -> {table[key]/len(table):.2f}%")

