import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os


homePath = os.getcwd()

def readFile():
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)


    os.chdir("../dataFiles")
    cropName = content[1].strip()
    os.chdir(homePath)
    os.chdir("../dataFiles/predictionResultFrames")
    D = pd.read_csv("yan_combinations_"+cropName+".csv")
    os.chdir(homePath)
    return D




if __name__ == "__main__":
    data = readFile()
    firstIndex = 7
    lastIndex = firstIndex + 16
    colNames = list(data)
    for i in range(firstIndex, lastIndex):
        plt.scatter(data["yield"],data[colNames[i]],label=None)
        plt.xlabel("Actual Yield")
        plt.ylabel("Yield from Model " + colNames[i])
        model_txt = colNames[i] + " ~ Q('yield')"
        func = smf.ols(model_txt, data = data, missing='drop').fit()
        # Change the range
        theRange = 100
        plt.xlim((0,theRange))
        plt.ylim((0,theRange))
        straight = [i for i in range (0,theRange,1)]
        plt.plot(straight, straight,'g-', label = "y = x")
        straightDf = pd.DataFrame(straight, columns = ['yield'])
        plt.plot(straight, func.predict(straightDf), 'r-',label='Predicted Yield vs. Actual Yield Best Fit')
        plt.legend(loc=2)
        plt.title("Predicted Yield versus Actual Yield")

        plt.savefig('figures/scatterPlots/scatter_plot_yield_against_%s'%colNames[i])

        plt.clf()



