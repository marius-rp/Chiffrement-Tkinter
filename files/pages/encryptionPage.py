from utils.additionalFunction import *
from utils.cleanupDisplay import destroy
from utils.logicFunctions import executionEncryption


def encryptionPage(frame, tk, text, descriptionText, recoveryTextEncryption):
    try:
        # Delete previous window
        destroy(frame)

        # Display of main elements
        mainElement = DisplayingMainElement(tk, frame, text)
        
        secondaryElement = DisplayingSecondaryElement(
            tk, mainElement, descriptionText, executionEncryption, recoveryTextEncryption)
    except:
        messageError(tk, mainElement, secondaryElement[0])