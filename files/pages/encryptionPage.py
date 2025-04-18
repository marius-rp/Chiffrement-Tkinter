from utils.additionalFunction import *
from utils.cleanupDisplay import destroy
from utils.logicFunctions import executionEncryption


def encryptionPage(frame, tk, text, descriptionText, recoveryTextEncryption, colorbg, police):
    try:
        # Delete previous window
        destroy(frame)

        # Display of main elements
        mainElement = DisplayingMainElement(tk, frame, text, colorbg, police)
        
        secondaryElement = DisplayingSecondaryElement(
            tk, mainElement, descriptionText, executionEncryption, recoveryTextEncryption, colorbg, police)
    except:
        messageError(tk, mainElement, secondaryElement[0], colorbg, police)