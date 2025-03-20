import tkinter as tk

window = tk.Tk()
window.title("Encryption")
window.geometry("480x360")
window.config(background='#adfeff')

#Menu
menu = tk.Menu (window)
fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Encryption", command="")
fileMenu.add_command(label="Decryption", command="")
menu.add_cascade(label="encryption", menu=fileMenu)
menu.add_command(label="close", command=window.quit)

window.config(menu=menu)

#Création des frame
frame = tk.Frame(window, bg='#adfeff')
frame.pack()
frameSecondary = tk.Frame(frame, bg='#adfeff')

#création des labels
label = tk.Label(frame, text="text", font=("Times New Roman", 20), bg='#adfeff', fg='black')
label.pack()

frameSecondary.pack()

labelSecondary = tk.Label(frameSecondary, text="textEncryption", font=("Times New Roman", 12), bg='#adfeff', fg='black')
entry = tk.Entry(frameSecondary, width=30)
button = tk.Button(frameSecondary, width=10, text="Valider", command="")
recovery = tk.Entry(frameSecondary, width=30)

labelSecondary.pack()
entry.pack()
button.pack()
recovery.pack()

window.mainloop()
