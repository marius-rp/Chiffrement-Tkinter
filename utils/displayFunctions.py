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
    text = ("This software allows you to encrypt and decrypt letters, words, phrases, and numbers in order to protect your data. It has its own encryption methods, and your key will be essential to decrypt the password. Decrypting data encrypted with this software using other software is useless, as it will not work.")
    return title, text

def resize_wrap(event, text_widget):
    text_widget.config(width=event.width - 5)
