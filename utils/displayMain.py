from utils.cleanupDisplay import destroy
from utils.displayFunctions import resize_wrap, textHome

def displayMain(frame, tk):
    destroy(frame)
    descriptiontextHome = textHome()

    # Titre
    titleFrame = tk.Frame(frame, bg='#adfeff')
    titleLabel = tk.Label(
        titleFrame,
        text=descriptiontextHome[0],
        font=("Times New Roman", 20),
        bg='#adfeff',
        fg='black'
    )
    titleFrame.pack()
    titleLabel.pack()

    # Description + Scroll
    frameSecondary = tk.Frame(frame, bg='#adfeff')
    frameSecondary.pack(fill="both", expand=True)

    # Scrollbar
    scrollbar = tk.Scrollbar(frameSecondary)
    scrollbar.pack(side="right", fill="y")

    # Text widget avec scrollbar
    descriptionText = tk.Text(
        frameSecondary,
        wrap="word",
        yscrollcommand=scrollbar.set,
        font=("Times New Roman", 14),
        bg='#adfeff',
        fg='black',
        borderwidth=0,
        highlightthickness=0
    )
    descriptionText.insert("1.0", descriptiontextHome[1])
    descriptionText.config(state="disabled") 
    descriptionText.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    scrollbar.config(command=descriptionText.yview)

    # Responsive wrap
    frameSecondary.bind("<Configure>", lambda event: resize_wrap(event, descriptionText))
