import tkinter as tk
from files.pages.decryptionPage import decryptionPage
from files.pages.encryptionPage import encryptionPage
from utils.additionalFunction import *
from utils.displayFunctions import *

#---------
### Initializing Tkinter ###
window = tk.Tk()
window.title("Encryption")
window.geometry("480x360")
window.config(background='#adfeff')
frame = tk.Frame(window, bg='#adfeff')
frame.pack()
#---------

#---------
### Text display ###

#Encryption
returnTextEncryption = textEncryption()
titleTextEncryption = returnTextEncryption[0]
descriptionTextEncryption = returnTextEncryption[1]
recoveryTextEncryption = returnTextEncryption[2]

#Decryption
returnTextDecryption = textDecryption()
titleTextDecryption = returnTextDecryption[0]
descriptionTextDecryption = returnTextDecryption[1]
recoveryTextDecryption = returnTextDecryption[2]
#---------

# Menu
menu = tk.Menu(window)
fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Encryption", command=lambda: encryptionPage(frame, tk, titleTextEncryption, descriptionTextEncryption, recoveryTextEncryption))
fileMenu.add_command(label="Decryption", command=lambda: decryptionPage(frame, tk, titleTextDecryption, descriptionTextDecryption, recoveryTextDecryption))
menu.add_cascade(label="encryption", menu=fileMenu)
menu.add_command(label="close", command=window.quit)

window.config(menu=menu)

window.mainloop()
