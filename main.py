import sys
import os
import tkinter as tk
from tkinter import PhotoImage as PI
from files.pages.decryptionPage import decryptionPage
from files.pages.encryptionPage import encryptionPage
from utils.displayMain import displayMain
from utils.additionalFunction import *
from utils.displayFunctions import *

#link transformation function for compilation
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#---------
### Initializing Tkinter ###
window = tk.Tk()
window.title("Encryption")
window.geometry("480x360")
window.minsize(320, 240)
window.maxsize(854, 480)
logo_path = resource_path("img/Padlock.png")
logo = PI(file=logo_path)
colorbg = "#d4d4b8"
police="Sans-Serif"
window.iconphoto(False, logo)
window.config(bg=colorbg)
frame = tk.Frame(window, bg=colorbg)
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
fileMenu.add_command(label="Home", command=lambda: displayMain(frame, tk, colorbg, police))
fileMenu.add_command(label="Encryption", command=lambda: encryptionPage(frame, tk, titleTextEncryption, descriptionTextEncryption, recoveryTextEncryption, colorbg, police))
fileMenu.add_command(label="Decryption", command=lambda: decryptionPage(frame, tk, titleTextDecryption, descriptionTextDecryption, recoveryTextDecryption, colorbg, police))
menu.add_cascade(label="encryption", menu=fileMenu)
menu.add_command(label="close", command=window.quit)

window.config(menu=menu)

displayMain(frame, tk, colorbg, police)

window.mainloop()
