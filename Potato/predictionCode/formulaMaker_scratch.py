
def addFixedEffects(desiredComponents, formulaString=""):
    '''
    Given a list of variants of predictors to add, render them into a model
    configuration string for use in Python or R, by interleaving the strings of
    variants with "+"

    param desiredComponents: An iterable of strings of variants of predictors to make
    a model configuration from
    param: An existing model configuration string (formula string) to append to

    return: The result of appending the passed in string with the formula string
    obtained by rendering variants in desiredComponents into a string
    '''

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

