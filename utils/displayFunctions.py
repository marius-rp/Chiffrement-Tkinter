### text definition ###
def textEncryption():
    text = "Encryption"
    descriptionText = "Enter your text to be encrypted : "
    recoveryText = "Encryption text : "
    return text, descriptionText, recoveryText


def textDecryption():
    text = "Decryption"
    descriptionText = "Enter your text to be decryption : "
    recoveryText = "Decryption text : "
    return text, descriptionText, recoveryText

def textHome():
    title = "Home encryption"
    text = ("This software allows you to encrypt and decrypt letters, words, sentences, numbers "
        "to protect your data. The software has its own encryption methods, and to decrypt the "
        "password, your key will be essential. Decrypting data encrypted with other software is "
        "useless because it won't work.")
    print(text)
    return title, text

def resize_wrap(event, text_widget):
    text_widget.config(width=event.width - 5)