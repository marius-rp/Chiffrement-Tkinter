import random

### Fonctions ###

"""-------------------------
Ecryption
-------------------------""" 

def encryptionEnd (text, decalage):
    try:
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + decalage - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + decalage - 97) % 26 + 97)
            else:
                result += char
        textEncryption= "Le texte à été chiffré avec succès"
        print(textEncryption, "green")
        return result
    except:
        textErreur= "Erreur dans le chiffrementdu texte"
        print(textErreur, "red")

def changeSpace(text):
    try:
        caracteres_possibles = ["*", "£", "$"]
        textModifie = "".join(random.choice(caracteres_possibles) if char == " " else char for char in text)
        return textModifie
    except:
        textErreur = "Erreur dans le chiffrement des espaces"
        print(textErreur, "red")

def executionEncryption (enter_user, decalage):
    EncryptionSpace= changeSpace(enter_user)
    print('changespace: ',EncryptionSpace)
    EncryptionCaesar = encryptionEnd(EncryptionSpace, decalage)
    print('encryptioncaesar: ',EncryptionCaesar)
    EncryptionASCII = hex(int.from_bytes(EncryptionCaesar.encode(), 'big'))
    print('fin: ',EncryptionASCII)
    return EncryptionASCII

"""-------------------------
Decryption
-------------------------""" 

def decryptionEnd(text, decalage):
    try:
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) - decalage - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - decalage - 97) % 26 + 97)
            else:
                result += char
        textEncryption = "Le texte à été chiffré avec succès"
        print(textEncryption)
        return result
    except:
        textErreur = "Erreur dans le chiffrementdu texte"
        print(textErreur, "red")


def addSpace(text):
    try:
        caracteresPossibles = ["*", "£", "$"]
        textModifie = "".join(
            " " if char in caracteresPossibles else char for char in text)
        return textModifie
    except:
        textErreur = "Erreur dans le chiffrement des espaces"
        print(textErreur, "red")

"""-------------------------
Execution
-------------------------"""

def executionEncryption (userInput, gap):
    encryptionSpace= changeSpace(userInput)
    encryptionCaesar = encryptionEnd(encryptionSpace, gap)
    encryptionASCII = hex(int.from_bytes(encryptionCaesar.encode(), 'big'))
    return encryptionASCII

def executionDecryption (userInput, gap):
    removeUnnecessaryCharacter = userInput[2:]
    decryptionASCII = bytes.fromhex(removeUnnecessaryCharacter).decode()
    descryptionCaesar = decryptionEnd(decryptionASCII, gap)
    descryptionSpace= addSpace(descryptionCaesar)
    return descryptionSpace

def  execution(userInput, gapInput, executionFunction, tk, mainElement, recoveryText):
    user = userInput.get()
    gap = int(gapInput.get())

    response = executionFunction(user, gap)

    labelRecovery = tk.Label(mainElement[1], text=recoveryText, font=(
        "Times New Roman", 12), bg='#adfeff', fg='black')
    recovery = tk.Entry(mainElement[1], width=30)
    recovery.insert(0, response)
    labelRecovery.pack()
    recovery.pack()