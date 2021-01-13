# Caesar Cipher Encryptor
# Example:
# String: "xyz", Key: 2
# Answer: "zab"

# ==============================================================

# O(N) Time | O(N) Space

def caesarCipherEncryptor(string, key):
    newKey = key % 26
    cipherLetters = []
    for letter in string:
        cipherLetters.append(getNewLetter(letter, newKey))
    return "".join(cipherLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    if newLetterCode <= 122:
        return chr(newLetterCode)
    else:
        return chr(96 + newLetterCode % 122)

# ==============================================================

# O(N) Time | O(N) Space

def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    #alphabets = list("zyxwvutsrqponmlkjihgfedcba") # For reverse shifting
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabets))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabets):
    newLetterCode = alphabets.index(letter) + key
    return alphabets[newLetterCode] if newLetterCode <= 25 else alphabets[-1 + newLetterCode % 25]

print(caesarCipherEncryptor("z", 52))
