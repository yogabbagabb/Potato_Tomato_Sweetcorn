import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os

homePath = os.getcwd()

def yield_trend(df, yield_type='rainfed'):
    '''
    Detrend a data frame using some function (ie quadratic or linear).
    param df: A raw data frame 
    param yield_type: The type of yield that we wish to detrend on
    '''
    trend_model_txt =  "Q('%s')"%"yield" + "~ np.power(year,2) + year"
    trend_results = smf.ols(trend_model_txt, data=df).fit()
    return trend_results

def endueAnomaly(D, trend_results):
    '''
    Give a data frame a yield anomaly.
    param D: A preprocessed data frame
    param trend_results: The fitted yield_trend function
    return: D, A preprocessed data frame with yield anomaly now defined
    '''
    D["yield_ana"] = D["yield"] - trend_results.predict(D)
    return D

def preprocesData():
    '''
    Read the appropriate csv (depending on the crop we're examining) and preprocess it.
    Then save it as "Crop Name"_with_anomaly.csv
    return: The preprocessed data file
    '''
    # Get the file from the
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)
    cropName = content[1].strip()


    # After getting a string from a file in a different directory, change back to our directory
    os.chdir("../dataFiles")
    data = pd.read_csv(content[0].strip())
    os.chdir(homePath)

    # The potato dataset has an anomaly: in 1987, Oregon saw about 8 entries
    # where yield exceeded 3000. For that reason, we exclude these entries.

    if (cropName == "potato"):
        data = data.loc[data["yield"] < 3000,:]

    # Add logical filter to the yield Data
    area_con = data['area'].notnull()
    data = data[area_con]
    

    # add growing season
    data['tave56789']= data.loc[:,'tave5':'tave9'].mean(axis=1)
    data['vpdave56789']= data.loc[:,'vpdave5':'vpdave8'].mean(axis=1)
    data['precip56789']= data.loc[:,'precip5':'precip9'].sum(axis=1)
    
    
    # Add z-score
    county_std = data.groupby('FIPS').std()['precip56789'].to_frame('precip_gs_std').reset_index()
    county_mean = data.groupby('FIPS').mean()['precip56789'].to_frame('precip_gs_mean').reset_index()
    
    data = data.merge(county_mean, on='FIPS').merge(county_std, on='FIPS')
    
    data['precip_gs_z'] = (data['precip56789'] - data['precip_gs_mean'])/data['precip_gs_std']

    # The 12 core states 
    trend_results = yield_trend(data)
    data = endueAnomaly(data, trend_results)
    os.chdir("../dataFiles")
    if (cropName == "potato"):
        data.to_csv("potato_with_anomaly.csv")
    if (cropName == "tomato"):
        data.to_csv("tomato_with_anomaly.csv")
    if (cropName == "sweetcorn"):
        data.to_csv("sweetcorn_with_anomaly.csv")
    os.chdir(homePath)

    return data

if __name__ == "__main__":
    D = preprocesData()
    
