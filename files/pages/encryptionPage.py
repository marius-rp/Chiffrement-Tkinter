from utils.additionalFunction import *
from utils.cleanupDisplay import destroy
from utils.logicFunctions import executionEncryption


def encryptionPage(frame, tk, text, descriptionText, recoveryTextEncryption):
    
    # Delete previous window
    destroy(frame)

    # Display of main elements
    mainElement = DisplayingMainElement(tk, frame, text)
    
    DisplayingSecondaryElement(
        tk, mainElement, descriptionText, executionEncryption, recoveryTextEncryption)