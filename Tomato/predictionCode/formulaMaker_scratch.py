
def addFixedEffects(desiredComponents, formulaString=""):
    theLength = len(desiredComponents)
    formulaString = "yield_ana ~ "
    for counter, component in enumerate(desiredComponents):
        formulaString += component
        if counter != (theLength -1):
            formulaString += " + "
    return formulaString

if __name__ == "__main__":
    compTwo = []
    comp = (('tave5', 'tave6', 'tave7'),
            ('tave5', 'tave6', 'tave8'),
            ('tave5', 'tave6', 'tave9'),
            ('tave5', 'tave7', 'tave8'),
            ('tave5', 'tave7', 'tave9'),
            ('tave5', 'tave8', 'tave9'),
            ('tave6', 'tave7', 'tave8'),
            ('tave6', 'tave7', 'tave9'),
            ('tave6', 'tave8', 'tave9'),
            ('tave7', 'tave8', 'tave9'),
            ('tave5', 'tave6', 'tave7', 'tave8'),
            ('tave5', 'tave6', 'tave7', 'tave9'),
            ('tave5', 'tave6', 'tave8', 'tave9'),
            ('tave5', 'tave7', 'tave8', 'tave9'),
            ('tave6', 'tave7', 'tave8', 'tave9'),
            ('tave5', 'tave6', 'tave7', 'tave8','tave9'))
    for component in comp:
        compTwo.append(addFixedEffects(component))
    print(compTwo)

