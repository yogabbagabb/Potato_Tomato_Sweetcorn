
def addFixedEffects_excl(desiredComponents, formulaString=""):
    '''
    Using only months months from may to august, create strings for certain
    predictors for use in model with fixed effects. Do NOT add linear terms
    if we desire a quadratic effect.

    param desiredComponents: The fixed effect predictors that we wish to use. See
    terminology for an explanation of what I mean by "predictors."

    param formulaString: A model configuration string that is being added to by this
    function.

    return: The concatenation of strings needed to express desiredComponents with
    formulaString
    '''
    theLength = len(desiredComponents)
    for counter, component in enumerate(desiredComponents):
        if component == "TAVE":
            formulaString += "tave5 +  tave6 +  tave7 +  tave8"
        if component == "TAVE2":
            formulaString += "I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2)"
        if component == "VPD":
            formulaString += "vpdave5 +  vpdave6 +  vpdave7 +  vpdave8"
        if component == "VPD2":
            formulaString += "I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2)"
        if component == "PRECIP":
            formulaString += "precip5 +  precip6 +  precip7 +  precip8"
        if component == "PRECIP2":
            formulaString += "I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2)"
        if component == "FIPS":
            formulaString += "FIPS"
        if counter != (theLength -1):
            formulaString += " + "
    return formulaString

def addFixedEffects(desiredComponents, formulaString=""):
    '''
    Using only months months from may to august, create strings for certain
    predictors for use in model with fixed effects. Do add linear terms
    if we desire a quadratic effect.

    param desiredComponents: The fixed effect predictors that we wish to use. See
    terminology for an explanation of what I mean by "predictors."

    param formulaString: A model configuration string that is being added to by this
    function.

    return: The concatenation of strings needed to express desiredComponents with
    formulaString
    '''

    theLength = len(desiredComponents)
    for counter, component in enumerate(desiredComponents):
        if component == "TAVE":
            formulaString += "tave5 +  tave6 +  tave7 +  tave8"
        if component == "TAVE2":
            formulaString += "tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2)"
        if component == "VPD":
            formulaString += "vpdave5 +  vpdave6 +  vpdave7 +  vpdave8"
        if component == "VPD2":
            formulaString += "vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2)"
        if component == "PRECIP":
            formulaString += "precip5 +  precip6 +  precip7 +  precip8"
        if component == "PRECIP2":
            formulaString += "precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2)"
        if component == "FIPS":
            formulaString += "FIPS"
        if counter != (theLength -1):
            formulaString += " + "
    return formulaString




def printString(fixedEffects, randomStateEffects, randomStateFIPSEffects):
    formulaString = "\"yield_ana ~ "
    if (fixedEffects != []):
        formulaString += addFixedEffects(fixedEffects)
    formulaString += "\""
    print(formulaString)


if __name__ == "__main__":
    fixedEffects = [["VPD","PRECIP"],["VPD","PRECIP2"],["VPD2","PRECIP"],["VPD2","PRECIP2"],
    ["TAVE","PRECIP"],["TAVE","PRECIP2"],["TAVE2","PRECIP"],["TAVE2","PRECIP2"],
    ["TAVE","PRECIP","VPD"],["TAVE","PRECIP2","VPD"],["TAVE2","PRECIP","VPD"],["TAVE2","PRECIP2","VPD"],["TAVE","PRECIP","VPD2"],["TAVE","PRECIP2","VPD2"],["TAVE2","PRECIP","VPD2"],["TAVE2","PRECIP2","VPD2"]]
    for i in range(len(fixedEffects)):
        print()
        printString(fixedEffects[i])
        print()

    


    
