import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os


homePath = os.getcwd()


def yield_trend(df, yield_type='rainfed'):
    # Estimate yield trend and detrend
    # Linear Trend
    trend_model_txt =  "Q('%s')"%"yield" + "~ year + np.power(year,2)"
    # Quadratic Trend
    # trend_model_txt =  "Q('%s')"%"yield" + "~ year + np.power(year,2)"
    trend_results = smf.ols(trend_model_txt, data=df).fit()
    return trend_results


def readFile():
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)


    os.chdir("../dataFiles")
    D = pd.read_csv(content[0].strip())
    os.chdir(homePath)

    # This dataset features some anomalies: in 1987, Oregon saw about 8 entries
    # where yield exceeded 3000. For that reason, we exclude these entries.

    D = D.loc[D["yield"] < 3000,:]

    cropName = content[1].strip()

    # The sweetcorn dataset includes an anomaly
    if (cropName == "sweetcorn"):
        D = D.loc[D["yield"] < 30,:]
    return D, cropName

def endueAnomaly(D, trend_results):
    D["yield_ana"] = D["yield"] - trend_results.predict(D)
    return D


if __name__ == "__main__":
    D,cropName = readFile()
    plt.figure(num=cropName)
    plt.scatter(D["year"], D["yield"])
    plt.xlabel("Year")
    plt.ylabel("Yield")
    trend_results = yield_trend(D)
    plt.title("Yield-Year Relationship for " + cropName)
    # sampleYears = pd.DataFrame([years for years in range(1997,2010)], index = "years")
    plt.plot(D["year"], trend_results.predict(D),'r-')
    print(D.loc[D["yield"] > 3000, :])
    plt.show()

    # Dprime = endueAnomaly(D, trend_results)
    # os.chdir("../dataFiles")
    # Dprime.to_csv("potato_with_anomaly.csv")
    # os.chdir(homePath)
