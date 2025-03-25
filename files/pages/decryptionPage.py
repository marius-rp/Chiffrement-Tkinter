from utils.additionalFunction import *
from utils.logicFunctions import executionDecryption


def decryptionPage(frame, tk, text, descriptionText, recoveryTextDecryption):

    # Delete previous window
    destroy(frame)

    # Display of main elements
    mainElement = DisplayingMainElement(tk, frame, text)

    returnInput = DisplayingSecondaryElement(
        tk, mainElement, descriptionText, lambda: executionDecryption(returnInput[0], returnInput[1]), recoveryTextDecryption)
