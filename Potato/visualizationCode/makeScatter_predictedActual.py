import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os


homePath = os.getcwd()

def readFile():
    '''
    Read the csv storing the predictions that yan desired into a data frame
    and return it.
    '''
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)


    cropName = content[1].strip()
    os.chdir("../dataFiles/predictionResultFrames")
    D = pd.read_csv("yan_combinations_"+cropName+".csv")
    os.chdir(homePath)
    return D




if __name__ == "__main__":
    data = readFile()
    # Define the first index of a column containing prediction data
    firstIndex = 7
    # Define the last index of a column containing prediction data
    lastIndex = firstIndex + 16
    colNames = list(data)
    # Plot the actual yield versus predicted yield for each model configuration
    # that falls between firstIndex and lastIndex (inclusive of endpoints) in the
    # csv called data. Save the resulting figure into a folder figures/scatterPlots/.
    for i in range(firstIndex, lastIndex):
        plt.scatter(data["yield"],data[colNames[i]],label=None)
        plt.xlabel("Actual Yield")
        plt.ylabel("Yield from Model " + colNames[i])
        model_txt = colNames[i] + " ~ Q('yield')"
        func = smf.ols(model_txt, data = data, missing='drop').fit()
        plt.xlim((0,800))
        plt.ylim((0,800))
        straight = [i for i in range (0,800,1)]
        plt.plot(straight, straight,'g-', label = "y = x")
        straightDf = pd.DataFrame(straight, columns = ['yield'])
        plt.plot(straight, func.predict(straightDf), 'r-',label='Predicted Yield vs. Actual Yield Best Fit')
        plt.legend(loc=2)
        plt.title("Predicted Yield versus Actual Yield")

        plt.savefig('figures/scatterPlots/scatter_plot_yield_against_%s'%colNames[i])

        plt.clf()



