import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os


homePath = os.getcwd()


def yield_trend(df, yield_type='rainfed'):
    # Estimate yield trend and detrend
    trend_model_txt =  "Q('%s')"%"yield" + "~ year + np.power(year,2)"
    print(trend_model_txt)
    # trend_model_txt =  "Q('%s')"%"yield" + "~ year + np.power(year,2)"
    trend_results = smf.ols(formula=trend_model_txt, data=df).fit()
    print(trend_results.summary())
    return trend_results


def readFile(predictorName):
    csvNameFile = ""
    if (predictorName == "Potato"):
        csvNameFile = "../Potato/csvNameFile.txt"
        dataDirectory = "../Potato/dataFiles"
    if (predictorName == "Tomato"):
        csvNameFile = "../Tomato/csvNameFile.txt"
        dataDirectory = "../Tomato/dataFiles"
    if (predictorName == "SweetCorn"):
        csvNameFile = "../SweetCorn/csvNameFile.txt"
        dataDirectory = "../SweetCorn/dataFiles"

    with open(csvNameFile) as f:
        content = f.readlines()

    os.chdir(dataDirectory)
    D = pd.read_csv(content[0].strip())
    os.chdir(homePath)

    # This dataset features some anomalies: in 1987, Oregon saw about 8 entries
    # where yield exceeded 3000. For that reason, we exclude these entries.

    if (predictorName == "Potato"):
        D = D.loc[D["yield"] < 3000,:]
    if (predictorName == "Tomato"):
        D = D.loc[D["yield"] < 60,:]
    if (predictorName == "SweetCorn"):
        D = D.loc[D["yield"] < 40,:]


    return D

def endueAnomaly(D, trend_results):
    D["yield_ana"] = D["yield"] - trend_results.predict(D)
    return D

def plotCrop(f,ax, cropName):
    D = readFile(cropName)
    f.canvas.set_window_title("Fruits and Vegetables")
    if cropName == "Potato":
        rowIndex = 0
    if cropName == "Tomato":
        rowIndex = 1
    if cropName == "SweetCorn":
        rowIndex = 2
    colIndex_avg = 0
    colIndex_reg = 1


    ax[rowIndex,colIndex_reg].plot(D["year"], D["yield"],'bo')
    ax[rowIndex,colIndex_reg].set_xlabel("Year")
    ax[rowIndex,colIndex_reg].set_ylabel("Yield")
    trend_results = yield_trend(D)
    ax[rowIndex,colIndex_reg].set_title("Yield-Year Relationship for " + cropName)

    ax[rowIndex,colIndex_reg].plot(D["year"], trend_results.predict(D),'r-')

    yearFrame = D.groupby(["year"]).mean()
    startYear = int(yearFrame.index.min())
    endYear = int(yearFrame.index.max()) + 1
    # years = [year for year in range(startYear, endYear ,1)]
    years = yearFrame.index
    ax[rowIndex,colIndex_avg].plot(years, [yearFrame.loc[year,"yield"] for year in years],'bo')

    ax[rowIndex,colIndex_avg].set_xlabel("Year")
    ax[rowIndex,colIndex_avg].set_ylabel("Average Yield over Year")
    ax[rowIndex,colIndex_avg].set_title("Average Yield-Year Relationship for " + cropName)

if __name__ == "__main__":
    f, ax = plt.subplots(3,2)
    plt.subplots_adjust(top=0.95, bottom=0.01, left=0.075, right=0.925, hspace=0.4)
    plotCrop(f,ax,"Potato")
    plotCrop(f,ax,"Tomato")
    plotCrop(f,ax,"SweetCorn")
    plt.show()

    # Potato


