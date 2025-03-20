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

def executionDecryption (enter_user, decalage):
    removeUnnecessaryCharacter = enter_user[2:]
    decryptionASCII = bytes.fromhex(removeUnnecessaryCharacter).decode()
    descryptionCaesar = decryptionEnd(decryptionASCII, decalage)
    descryptionSpace= addSpace(descryptionCaesar)
    print(descryptionSpace)