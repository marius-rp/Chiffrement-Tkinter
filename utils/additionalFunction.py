# Removing window elements
from utils.messageError import messageError
from utils.logicFunctions import execution

# Generation of main frames and title
def DisplayingMainElement(tk, frame, text, colorbg, police):
    titleFrame = tk.Frame(frame, bg=colorbg)
    frameSecondary = tk.Frame(frame, bg=colorbg)
    titleLabel = tk.Label(titleFrame, text=text, font=(
        police, 20), bg=colorbg, fg='black')
    titleFrame.pack()
    titleLabel.pack()
    frameSecondary.pack()
    return titleFrame, frameSecondary

# Generation of secondary frames and texts
def DisplayingSecondaryElement(tk, mainElement, descriptionText, executionFunction, recoveryText, colorbg, police):
    try:
        textGap = "Encryption key : "

        labelEntry = tk.Label(mainElement[1], text=descriptionText, font=(
            police, 12), bg=colorbg, fg='black')
        labelgap = tk.Label(mainElement[1], text=textGap, font=(
            police, 12), bg=colorbg, fg='black')

        userInput = tk.Entry(mainElement[1], width=30)
        gapInput = tk.Entry(mainElement[1], width=5)
        responseFrame = tk.Frame(mainElement[1], bg=colorbg)

        labelEntry.pack()
        userInput.pack()
        labelgap.pack()
        gapInput.pack()

        button = tk.Button(mainElement[1], width=10, text="Valider", cursor="hand2", command=lambda: execution(
            userInput, gapInput, executionFunction, tk, responseFrame, recoveryText, mainElement, colorbg, police))
        button.pack(pady=(10, 0))
    except:
        textError = "Error in display Secondary Element"
        responseError = messageError(tk, mainElement, textError, colorbg, police)
        return responseError