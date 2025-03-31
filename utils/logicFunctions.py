import random

from utils.cleanupDisplay import destroy

### Fonctions ###

"""-------------------------
Ecryption
-------------------------"""


def encryptionEnd(text, decalage):
    try:
        result = ""
        for char in text:
            if char.isalpha():
                result += chr(ord(char) + decalage)
            else:
                result += char
        return result
    except Exception as e:
        print(f"Error in text encryption: {e}")
        return None


def changeSpace(text):
    try:
        caracteres_possibles = ["*", "£", "$"]
        textModifie = "".join(random.choice(
            caracteres_possibles) if char == " " else char for char in text)
        return textModifie
    except:
        textError = "Error in the encryption of spaces"
        print(textError, "red")


"""-------------------------
Decryption
-------------------------"""


def decryptionEnd(text, decalage):
    try:
        result = ""
        for char in text:
            if char.isalpha():
                result += chr(ord(char) - decalage)
            else:
                result += char
        return result
    except Exception as e:
        textError = f"Error in text decryption: {e}"
        print(textError, "red")
        return None


def addSpace(text):
    try:
        caracteresPossibles = ["*", "£", "$"]
        textModifie = "".join(
            " " if char in caracteresPossibles else char for char in text)
        return textModifie
    except:
        textError = "Error in the encryption of spaces"
        print(textError, "red")


"""-------------------------
Execution
-------------------------"""


def executionEncryption(userInput, gap):
    try:
        encryptionSpace = changeSpace(userInput)
        encryptionCaesar = encryptionEnd(encryptionSpace, gap)
        encryptionASCII = hex(int.from_bytes(encryptionCaesar.encode(), 'big'))
        return encryptionASCII
    except Exception as err:
        textError = f"Error in execution: {err}"
        print(textError, "red")


def executionDecryption(userInput, gap):
    try:
        removeUnnecessaryCharacter = userInput[2:]
        decryptionASCII = bytes.fromhex(removeUnnecessaryCharacter).decode()
        descryptionCaesar = decryptionEnd(decryptionASCII, gap)
        descryptionSpace = addSpace(descryptionCaesar)
        return descryptionSpace
    except Exception as err:
        textError = f"Error in decryption: {err}"
        print(textError, "red")


def execution(userInput, gapInput, executionFunction, tk, responseFrame, recoveryText):
    try:
        responseFrame.pack()
        destroy(responseFrame)

        user = userInput.get()
        gap = int(gapInput.get())

        response = executionFunction(user, gap)

        labelRecovery = tk.Label(responseFrame, text=recoveryText, font=(
            "Times New Roman", 12), bg='#adfeff', fg='black')
        recovery = tk.Entry(responseFrame, width=30)
        recovery.insert(0, response)
        labelRecovery.pack()
        recovery.pack()
    except:
        textError = "Error in frame display"
        print(textError)