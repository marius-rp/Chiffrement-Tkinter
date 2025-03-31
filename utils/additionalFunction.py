# Removing window elements
from utils import messageError
from utils.logicFunctions import execution

# Generation of main frames and title
def DisplayingMainElement(tk, frame, text):
    titleFrame = tk.Frame(frame, bg='#adfeff')
    frameSecondary = tk.Frame(frame, bg='#adfeff')
    titleLabel = tk.Label(titleFrame, text=text, font=(
        "Times New Roman", 20), bg='#adfeff', fg='black')
    titleFrame.pack()
    titleLabel.pack()
    frameSecondary.pack()
    return titleFrame, frameSecondary

# Generation of secondary frames and texts
def DisplayingSecondaryElement(tk, mainElement, descriptionText, executionFunction, recoveryText):
    try:
        textGap = "Encryption key : "

        labelEntry = tk.Label(mainElement[1], text=descriptionText, font=(
            "Times New Roman", 12), bg='#adfeff', fg='black')
        labelgap = tk.Label(mainElement[1], text=textGap, font=(
            "Times New Roman", 12), bg='#adfeff', fg='black')

        userInput = tk.Entry(mainElement[1], width=30)
        gapInput = tk.Entry(mainElement[1], width=5)
        responseFrame = tk.Frame(mainElement[1], bg='#adfeff')

        labelEntry.pack()
        userInput.pack()
        labelgap.pack()
        gapInput.pack()

        button = tk.Button(mainElement[1], width=10, text="Valider", cursor="hand2", command=lambda: execution(
            userInput, gapInput, executionFunction, tk, responseFrame, recoveryText, mainElement))
        button.pack()
    except:
        textError = "Error in display Secondary Element"
        responseError = messageError(tk, mainElement, textError)
        return responseError