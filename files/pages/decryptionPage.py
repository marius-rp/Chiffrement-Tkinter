from utils.additionalFunction import *
from utils.cleanupDisplay import destroy
from utils.logicFunctions import executionDecryption


def decryptionPage(frame, tk, text, descriptionText, recoveryTextDecryption, colorbg, police):

    try:
        # Delete previous window
        destroy(frame)

        # Display of main elements
        mainElement = DisplayingMainElement(tk, frame, text, colorbg, police)

        secondaryElement = DisplayingSecondaryElement(
            tk, mainElement, descriptionText, executionDecryption, recoveryTextDecryption, colorbg, police)
    except:
        messageError(tk, mainElement, secondaryElement[0], colorbg, police)