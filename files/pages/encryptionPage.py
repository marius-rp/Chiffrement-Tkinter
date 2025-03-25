import time
from utils.additionalFunction import *
from utils.logicFunctions import executionEncryption


def encryptionPage(window, tk, text, descriptionText, recoveryTextEncryption):

    # Delete previous window
    #destroy(frame)
    
    # Display of main elements
    mainElement = DisplayingMainElement(tk, window, text)
    returnInput = DisplayingSecondaryElement(
        tk, mainElement, descriptionText, lambda: executionEncryption(returnInput[0], returnInput[1]), recoveryTextEncryption)