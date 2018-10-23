import numpy as np
import pandas as pd
import os

homePath = os.getcwd()


def printRMSEMedian():
    '''
    After specifying the rmse csv files (ie those files in which we stored the rmses of 
    function predictions), calculate and print the median for each
    set of files
    '''
    csvFiles = ["tave_evi_squared_rmse.csv"]

    for file in csvFiles:
        A = pd.read_csv(file)
        A = A.iloc[:,1:]
        print(A.median())

def calculateR2Python(csvFiles):
    '''
    Background: Yan's python prediction code saved predictions into a column called
    "Predicted_yield_ana." Other code then compared these predictions with entries in a column
    called "yield_ana" in order to compute statistics like RMSE, R^2 etc. This function
    performs these computations and prints the resulting statistics for a passed in
    set of filenames that correspond to csvs obtained from, among other sources, performing predictions using
    Yan's prediction code. Really, these csvs can have been obtained from anywhere; they must have a "Predicted_yield_ana" field and a "yield_ana" field.

    param: csvFiles: An iterable consisting of strings of csv file names; in these csvs predicted yields have been stored.
    '''
    for aFile in csvFiles:
        modelFrame = pd.read_csv(aFile)
        # Get the column names from the data frame
        colNames = ["yield_ana"]
        for model in colNames:

            result = pd.DataFrame(np.full([modelFrame['year'].unique().shape[0],3], np.nan), index=modelFrame['year'].unique(), columns=['R2','rmse','R2_classic'])

            for y in range(modelFrame['year'].min(), modelFrame['year'].max()+1):
                con = modelFrame['year']==y
                yieldType = "Predicted_yield_ana"
                r2_temp = modelFrame.loc[con,[yieldType, \
                                        model]].corr() \
                    [model][0]**2
                
                # N is the sample number after removing nan
                N = modelFrame.loc[con,[yieldType,model]].dropna().shape[0]
                rmse_temp = (((modelFrame.loc[con, model] -  \
                                  modelFrame.loc[con, yieldType])**2).sum() \
                                              /N)**0.5
                                          #    /modelFrame.loc[con,yieldType].shape[0])**0.5
                             
        #                                       /modelFrame.loc[con,model].shape[0])**0.5

                sst = ((modelFrame.loc[con, yieldType] \
                        - modelFrame.loc[con, yieldType].mean())**2).sum()
                sse = ((modelFrame.loc[con, yieldType] - modelFrame.loc[con, model])**2).sum()

                result.loc[y] = [r2_temp, rmse_temp, 1-sse/sst]
            print(model)
            # print(result)
            print(result.median()['rmse'])
            print(result.median()['R2'])

def calculateR2(csvFiles):
    '''
    Background: Aahan's prediction code saved predictions for a certain model into a column
    with the same name of the model. Note that Aahan's predictions were "predicted_yield"
    and not "predicted_yield_ana" -- that is, his R code adds back the yield anomaly.

    Other code then compared these predictions with entries in a columnk
    called "yield" in order to compute statistics like RMSE, R^2 etc. This function
    performs these computations and prints the resulting statistics for a passed in
    set of filenames that correspond to csvs obtained from, among other sources, performing predictions using
    Aahan's R prediction code. Really, these csvs can have been obtained from anywhere; they must have only predicted total yields in columns starting at the 7th (counting off from 0) index and a "yield" field.

    param: csvFiles: An iterable consisting of strings of csv file names; in these csvs predicted yields have been stored.
    '''
    indexOfFirstModel = 7
    for aFile in csvFiles:
        modelFrame = pd.read_csv(aFile)
        # Get the column names from the data frame
        colNames = list(modelFrame)
        for model in colNames[indexOfFirstModel::]:

            result = pd.DataFrame(np.full([modelFrame['year'].unique().shape[0],3], np.nan), index=modelFrame['year'].unique(), columns=['R2','rmse','R2_classic'])

            for y in range(modelFrame['year'].min(), modelFrame['year'].max()+1):
                con = modelFrame['year']==y
                yieldType = "yield"
                r2_temp = modelFrame.loc[con,[yieldType, \
                                        model]].corr() \
                    [model][0]**2
                
                # N is the sample number after removing nan
                N = modelFrame.loc[con,[yieldType,model]].dropna().shape[0]
                rmse_temp = (((modelFrame.loc[con, model] -  \
                                  modelFrame.loc[con, yieldType])**2).sum() \
                                              /N)**0.5
                                          #    /modelFrame.loc[con,yieldType].shape[0])**0.5
                             
        #                                       /modelFrame.loc[con,model].shape[0])**0.5

                sst = ((modelFrame.loc[con, yieldType] \
                        - modelFrame.loc[con, yieldType].mean())**2).sum()
                sse = ((modelFrame.loc[con, yieldType] - modelFrame.loc[con, model])**2).sum()

                result.loc[y] = [r2_temp, rmse_temp, 1-sse/sst]
            print(model)
            # print(result)
            print(result.median()['rmse'])
            print(result.median()['R2'])





if __name__ == "__main__":
    calculateR2Python(["python_temp_model_A"])
