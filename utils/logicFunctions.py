import random
from utils.messageError import messageError
from utils.cleanupDisplay import destroy

### Fonctions ###

"""-------------------------
Ecryption
-------------------------"""


def encryptionEnd(text, decalage, tk, mainElement, colorbg, police):
    try:
        result = ""
        for char in text:
            if char.isalpha():
                result += chr(ord(char) + decalage)
            else:
                result += char
        return result
    except Exception as e:
        textError = "Error in end encryption"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError


def changeSpace(text, tk, mainElement, colorbg, police):
    try:
        caracteres_possibles = ["*", "£", "$"]
        textModifie = "".join(random.choice(
            caracteres_possibles) if char == " " else char for char in text)
        return textModifie
    except:
        textError = "Error in the encryption of spaces"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError

"""-------------------------
Decryption
-------------------------"""


def decryptionEnd(text, decalage, tk, mainElement, colorbg, police):
    try:
        result = ""
        for char in text:
            if char.isalpha():
                result += chr(ord(char) - decalage)
            else:
                result += char
        return result
    except Exception as e:
        textError = "Error in text end decryption"
        responseError = messageError(tk, mainElement, textError)
        return responseError


def addSpace(text, tk, mainElement, colorbg, police):
    try:
        caracteresPossibles = ["*", "£", "$"]
        textModifie = "".join(
            " " if char in caracteresPossibles else char for char in text)
        return textModifie
    except:
        textError = "Error in the encryption of spaces"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError


"""-------------------------
Execution
-------------------------"""


def executionEncryption(userInput, gap, tk, mainElement, colorbg, police):
    try:
        encryptionSpace = changeSpace(userInput, tk, mainElement, colorbg, police)
        encryptionCaesar = encryptionEnd(encryptionSpace, gap, tk, mainElement, colorbg, police)
        encryptionASCII = hex(int.from_bytes(encryptionCaesar.encode(), 'big'))
        return encryptionASCII
    except Exception as err:
        textError = "Error in execution encryption"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError


def executionDecryption(userInput, gap, tk, mainElement, colorbg, police):
    try:
        removeUnnecessaryCharacter = userInput[2:]
        decryptionASCII = bytes.fromhex(removeUnnecessaryCharacter).decode()
        descryptionCaesar = decryptionEnd(decryptionASCII, gap, tk, mainElement, colorbg, police)
        descryptionSpace = addSpace(descryptionCaesar, tk, mainElement, colorbg, police)
        return descryptionSpace
    except Exception as err:
        textError = "Error in decryption"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError


def execution(userInput, gapInput, executionFunction, tk, responseFrame, recoveryText, mainElement, colorbg, police):
    try:
        responseFrame.pack(pady=(20, 0))
        destroy(responseFrame)

        user = userInput.get()
        gap = int(gapInput.get())
        response = executionFunction(user, gap, tk, mainElement, colorbg, police)

        labelRecovery = tk.Label(responseFrame, text=recoveryText, font=(
            police, 12), bg=colorbg, fg='black')
        recovery = tk.Entry(responseFrame, width=30)
        recovery.insert(0, response)
        labelRecovery.pack()
        recovery.pack()
    except:
        textError = "Error in frame display"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError