#:cd %:h
#head 

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
lowess = sm.nonparametric.lowess
import os


homePath = os.getcwd()


def load_yield_data():
    # Get the name of the crop we wish to examine
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)
    cropName = content[1].strip("\n").strip("\t")

    # Load the preprocessed data that we wish to examine
    data = pd.read_csv("../dataFiles/" + cropName + "_with_anomaly.csv",dtype={'FIPS':str})
    return data

def printOffByOne():
    '''
    Depict the knots appearing on a lowess curve for hardcoded variants of predictors
    one at a time, so that we can look at them more clearly.
    '''
    data = load_yield_data()
    numberColumns = 5

    # Define the first and lst string that will appear in an array of variables that
    # we wish to visualize lowess curves + knots for
    firstEntry = 'tmax5'
    lastEntry = 'precip9'
    colNames = list(data)
    # Get the corresponding indices (in the columns of hte data frame)
    # for the first and last string appearing in aforementioned
    # array of variables
    firstIndex =colNames.index(firstEntry)
    lastIndex = colNames.index(lastEntry)
    numberTypesOfVariables = 5
    months = 5
    # Specify the variables that week to plot knots atop lowess curves for
    variables = ['tave5', 'tave6', 'tave7', 'tave8', 'tave9', 'vpdave5', 'vpdave6', 'vpdave7', 'vpdave8', 'vpdave9', 'precip5', 'precip6', 'precip7', 'precip8', 'precip9']

    # Specify the knots ((x,y) coordinates) of the selected predictors
    tave5Knots = [(11.433,117.610),(13.5398,-14.5927),(15.5924,-12.5801),(20.123,-115.226)]
    tave6Knots = [(15.434,21.635),(20.7844,-26.6687),(25.129,-127.302)]
    tave7Knots = [(19.730,-10.567),(21.224,-0.504),(23.179,-10.567),(27.604,-131.327)]
    tave8Knots = [(18.980,-4.529),(21.866,-2.517),(26.7816,-133.34)]
    tave9Knots = [(13.1332,1.509),(14.432,14.585),(17.679,-8.555),(23.170,-125.289)]

    vpdave5Knots = [(10.364,-38.745),(16.366,80.002)]
    vpdave6Knots = [(6.824,-22.643),(11.975,-30.694),(21.124,102.142)]
    vpdave7Knots = [(8.816,-22.643),(13.071,-34.719),(24.728,102.142)]
    # vpdave8Knots = [(8.06,4.50),(9.10,3.31)]
    vpdave8Knots = [(7.626,-12.580),(9.482,-46.795),(22.801,102.142)]
    vpdave9Knots = [(9.107,-44.782),(17.883,120.256)]

    precip5Knots = [(44.3457,5.534)]
    # precip6Knots = [(92.6,0.50),(182.2,0.707)]
    precip6Knots = [(87.768,-32.707)]
    # precip7Knots = [(56.191,-2.08),(89.1428,0.492)]
    precip7Knots = [(50.357,-12.580)]
    precip8Knots = [(50.607,-16.605),(95.075,-28.681)]
    # precip9Knots = [(29.9037,-0.8919),(61,1.307),(104.1,1.30)]
    precip9Knots = [(29.078,-0.504),(122.595,-32.707)]


    # container = [vpdave6Knots, vpdave7Knots, vpdave8Knots, precip6Knots, precip7Knots, precip8Knots, precip9Knots]
    container = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(variables)):
        plt.plot(data[variables[i]], data["yield_ana"],'bx')
        plt.title([variables[i]])
        Z = lowess(data['yield_ana'], data[variables[i]],frac=0.3,it=3)
        plt.plot(Z[:,0], Z[:,1], 'g-', lw=5)
        knotBox = container[i]
        for (x,y) in knotBox:
            plt.plot(x,y, 'ro')
        fig = plt.gcf()
        plt.xlabel(variables[i])
        plt.ylabel('Yield anomaly (bu/ac)')
        fig.canvas.set_window_title(variables[i])
        plt.title("Response for %s"%(variables[i]))
        plt.show()
        # plt.savefig('./figures/knots/%s.png'%variables[i])
        plt.clf()


def printAll():
    '''
    Depict all lowess curves for hardcoded variants of predictors
    in one visualization, so that we can look at them more clearly.
    '''
    data = load_yield_data()
    numberColumns = 5
    # Define the first and lst string that will appear in an array of variables that
    # we wish to visualize lowess curves + knots for
    firstEntry = 'tmax5'
    lastEntry = 'lstmax9'
    colNames = list(data)
    # Get the corresponding indices (in the columns of hte data frame)
    # for the first and last string appearing in aforementioned
    firstIndex =colNames.index(firstEntry)
    lastIndex = colNames.index(lastEntry)
    numberTypesOfVariables = 5
    months = 5
    f, axarr = plt.subplots(numberTypesOfVariables, months)
    # Specify the variables that week to plot knots atop lowess curves for
    variables = ['tave5', 'tave6', 'tave7', 'tave8', 'tave9', 'vpdave5', 'vpdave6', 'vpdave7', 'vpdave8', 'vpdave9', 'precip5', 'precip6', 'precip7', 'precip8', 'precip9', 'evi5', 'evi6', 'evi7', 'evi8', 'evi9', 'lstmax5', 'lstmax6', 'lstmax7', 'lstmax8', 'lstmax9']
    # Print all lowess curves in one panoramic diagram
    for i in range(len(variables)):
            axarr[int(i/numberColumns), int(i%numberColumns)].plot(data[variables[i]], data["yield_rainfed_ana"],'bx')
            axarr[int(i/numberColumns), int(i%numberColumns)].set_title([variables[i]])
            Z = lowess(data['yield_rainfed_ana'], data[variables[i]],frac=0.3,it=3)
            axarr[int(i/numberColumns), int(i%numberColumns)].plot(Z[:,0], Z[:,1], 'g-', lw=5)


    plt.show()

if __name__ == "__main__":
    # printAll()
    printOffByOne()

