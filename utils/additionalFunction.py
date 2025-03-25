# Removing window elements
def destroy(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Generation of main frames and title
def DisplayingMainElement(tk, frame, text):
    titleFrame = tk.Frame(frame, bg='#adfeff')
    frameSecondary = tk.Frame(titleFrame, bg='#adfeff')
    titleLabel = tk.Label(titleFrame, text=text, font=(
        "Times New Roman", 20), bg='#adfeff', fg='black')
    titleFrame.pack()
    titleLabel.pack()
    frameSecondary.pack()
    return titleFrame, frameSecondary

# Generation of secondary frames and texts
def DisplayingSecondaryElement(tk, mainElement, descriptionText, functionDefined, recoveryText):

    textGap = "Encryption key : "

    labelEntry = tk.Label(mainElement[1], text=descriptionText, font=(
        "Times New Roman", 12), bg='#adfeff', fg='black')
    labelRecovery = tk.Label(mainElement[1], text=recoveryText, font=(
        "Times New Roman", 12), bg='#adfeff', fg='black')
    labelgap = tk.Label(mainElement[1], text=textGap, font=(
        "Times New Roman", 12), bg='#adfeff', fg='black')
    
    userInput = tk.Entry(mainElement[1], width=30)
    gapInput = tk.Entry(mainElement[1], width=5)
    button = tk.Button(mainElement[1], width=10, text="Valider", command=lambda: functionDefined)
    recovery = tk.Entry(mainElement[1], width=30)

    labelEntry.pack()
    userInput.pack()
    labelgap.pack()
    gapInput.pack()
    button.pack()
    labelRecovery.pack()
    recovery.pack()
    return userInput.get(), gapInput.get()